"""
Provide delivery date calculations based on declarative scheduling rules.

Rules adjust a starting datetime using offset, threshold-based,
weekday-based, monthly, or quarterly patterns.
"""
from datetime import datetime, timedelta


def _normalize(start: datetime, cfg: dict) -> datetime:
    """Keep minutes for offset rules, truncate for other rules."""
    if cfg.get("func") == _apply_offset:
        return start.replace(second=0, microsecond=0)
    return start.replace(minute=0, second=0, microsecond=0)


def _apply_offset(start: datetime, cfg: dict) -> datetime:
    """Apply a simple hour-based offset to the start datetime."""
    return start + timedelta(hours=cfg["hours"])


def _apply_threshold(start: datetime, cfg: dict) -> datetime:
    """Apply a time-of-day threshold rule to shift the delivery."""
    if start.hour < cfg["limit_hour"]:
        return start.replace(hour=cfg["before"])
    next_day = start + timedelta(days=1)
    return next_day.replace(hour=cfg["after"])


def _apply_weekend(start: datetime, cfg: dict) -> datetime:
    """
    Adjust the provided datetime based on weekend-related business logic.

    Handle three distinct modes:
    - EOW: Shift dates using a 'limit_day' threshold to define business hours.
    - Month: Ensure the date falls on a weekday by shifting forward to Monday.
    - Quarter: Ensure the date falls on a weekday by shifting backward to Friday.

    Args:
        start: The initial datetime object to be adjusted.
        cfg: A dictionary containing rule parameters.

    Returns:
        The adjusted datetime object.
    """
    weekday = start.weekday()
    limit_day = cfg.get("limit_day")
    
    # End-of-Week (EOW) rules
    if limit_day is not None:
        if weekday < limit_day:
            return (start + timedelta(days=4 - weekday)).replace(hour=cfg["weekday"])
        return (start + timedelta(days=6 - weekday)).replace(hour=cfg["weekend"])
    
    # Month (M) and Quarter (Q) rules
    if cfg.get("direction", 0) != 0:
        if weekday >= 5:
            days = (7 - weekday) if cfg["direction"] == 1 else (weekday - 4)
            return start + (days * cfg["direction"] * timedelta(days=1))
    
    return start


def _apply_month(start: datetime, cfg: dict) -> datetime:
    """Calculate the first day of the target month and adjust for weekends."""
    year = start.year + (1 if start.month >= cfg["months"] else 0)
    target = datetime(year, cfg["months"], 1, cfg["start_hour"])
    
    return _apply_weekend(target, cfg)


def _apply_quarter(start: datetime, cfg: dict) -> datetime:
    """Calculate the last day of the target quarter and adjust for weekends."""
    end_month = cfg["months"]
    year = start.year + (1 if start.month > end_month else 0)
    
    if end_month == 12:
        target = datetime(year + 1, 1, 1, cfg["start_hour"])
    else:
        target = datetime(year, end_month + 1, 1, cfg["start_hour"])
    target -= timedelta(days=1)
    
    return _apply_weekend(target, cfg)


RULES: dict[str, dict] = {
    "NOW": {"func": _apply_offset, "hours": 2},
    "ASAP": {"func": _apply_threshold, "limit_hour": 13, "before": 17, "after": 13},
    "EOW": {"func": _apply_weekend, "limit_day": 3, "weekday": 17, "weekend": 20},
    "M": {"func": _apply_month, "months": 1, "start_hour": 8, "direction": 1},
    "Q": {"func": _apply_quarter, "months": 3, "start_hour": 8, "direction": -1},
}


def _resolve(description: str) -> dict:
    """Resolve a symbolic rule into a configuration dictionary."""
    if description.endswith("M"):
        return {**RULES["M"], "months": int(description[:-1])}
    if description.startswith("Q"):
        factor = RULES["Q"]["months"]
        index = int(description[1:])
        return {**RULES["Q"], "months": index * factor}
    if description in RULES:
        return dict(RULES[description])
    
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
    
    