"""
Provide delivery date calculations based on declarative scheduling rules.

Rules adjust a starting datetime using offset, threshold-based,
weekday-based, monthly, or quarterly patterns.
"""
from datetime import datetime, timedelta


def _normalize(start: datetime, cfg: dict) -> datetime:
    """Keep minutes for offset rules, truncate for business rules."""
    if cfg.get("type") == "offset":
        return start.replace(second=0, microsecond=0)
    return start.replace(minute=0, second=0, microsecond=0)


def _apply_offset(start: datetime, cfg: dict) -> datetime:
    """Apply a simple hour-based offset to the start datetime."""
    return start + timedelta(hours=cfg["hours"])


def _apply_threshold(start: datetime, cfg: dict) -> datetime:
    """Apply a time-of-day threshold rule to shift the delivery."""
    if start.hour < cfg["limit"]:
        return start.replace(hour=cfg["before"])
    next_day = start + timedelta(days=1)
    return next_day.replace(hour=cfg["after"])


def _apply_weekend(start: datetime, cfg: dict) -> datetime:
    """Move delivery date to end of week based on a weekday limit."""
    weekday = start.weekday()

    if weekday < cfg["limit"]:
        target = start + timedelta(days=4 - weekday)
        return target.replace(hour=cfg["weekday"])

    target = start + timedelta(days=6 - weekday)
    return target.replace(hour=cfg["weekend"])


def _apply_month_or_quarter(start: datetime, cfg: dict) -> datetime:
    """Apply a monthly or quarterly rule using direct delta math.

    For months, it shifts the date to the 1st of the target month
    and moves forward to Monday if it lands on a weekend. For
    quarters, it uses a modulo rollover trick to target the 1st
    of the following month, subtracts one day to hit the quarter's
    end, and steps backward to Friday if necessary.
    """
    period = cfg["period"]
    is_quarter = cfg["type"] == "quarter"

    target_month = ((period % 4) * 3 + 1) if is_quarter else period
    target_year = start.year + (target_month <= start.month)
    
    target = datetime(target_year, target_month, 1, cfg["start_hour"])

    if is_quarter:
        target -= timedelta(days=1)
        if target.weekday() >= 5:
            target -= timedelta(days=target.weekday() % 4)
    else:
        if target.weekday() >= 5:
            target += timedelta(days=7 - target.weekday())

    return target


RULES: dict[str, dict] = {
    "NOW": {"func": _apply_offset, "hours": 2},
    "ASAP": {"func": _apply_threshold, "limit": 13, "before": 17, "after": 13},
    "EOW": {"func": _apply_weekend, "limit": 3, "weekday": 17, "weekend": 20},
    "M": {"func": _apply_month_or_quarter, "type": "month", "period": 1, "start_hour": 8},
    "Q": {"func": _apply_month_or_quarter, "type": "quarter", "period": 1, "start_hour": 8},
}


def _resolve(description: str) -> dict:
    """Resolve a symbolic rule into a configuration dictionary."""
    if description in RULES:
        return RULES[description]
    if description.endswith("M"):
        return {**RULES["M"], "period": int(description[:-1])}
    if description.startswith("Q"):
        return {**RULES["Q"], "period": int(description[1:])}
    raise ValueError(f"No rule defined for: {description}")


def delivery_date(start_iso: str, description: str) -> str:
    """Calculate final delivery date based on start timestamp and rule.

    Resolves the provided symbolic rule description, normalizes the
    minutes and seconds depending on the rule type, and invokes the
    responsible calculation handler to determine the final timestamp.

    Args:
        start_iso: The initial timestamp formatted as an ISO 8601
            string.
        description: A symbolic rule token (e.g., 'NOW', 'ASAP',
            '3M', 'Q2').

    Returns:
        The calculated delivery date and time formatted as an
        ISO 8601 string.

    Raises:
        ValueError: If the provided rule description cannot be
            resolved.
    """
    cfg = _resolve(description)
    start = _normalize(datetime.fromisoformat(start_iso), cfg)
    
    return cfg["func"](start, cfg).isoformat()
    