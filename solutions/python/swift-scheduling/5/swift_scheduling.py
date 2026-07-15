"""
Provide delivery date calculations based on declarative scheduling rules.

Rules adjust a starting datetime using offset, threshold-based,
weekday-based, monthly, or quarterly patterns.
"""
from datetime import datetime, timedelta
from typing import Dict, Any


RULES: Dict[str, Dict[str, Any]] = {
    "NOW": {"type": "offset", "hours": 2},
    "ASAP": {"type": "threshold", "limit": 13, "before": 17, "after": 13},
    "EOW": {"type": "weekend", "limit": 3, "weekday": 17, "weekend": 20},
    "M": {"type": "month", "period": 1, "start_hour": 8},
    "Q": {"type": "quarter", "period": 1, "start_hour": 8},
}


def _normalize(start: datetime) -> datetime:
    return start.replace(minute=0, second=0, microsecond=0)


def _apply_offset(start: datetime, cfg: Dict[str, Any]) -> datetime:
    return start + timedelta(hours=cfg["hours"])


def _apply_threshold(start: datetime, cfg: Dict[str, Any]) -> datetime:
    """
    Apply a time-of-day threshold rule.

    If the hour is below the limit, set the datetime to the 'before' hour.
    Otherwise move to the next day and set the 'after' hour.
    """
    if start.hour < cfg["limit"]:
        return start.replace(hour=cfg["before"])
    next_day = start + timedelta(days=1)
    return next_day.replace(hour=cfg["after"])


def _apply_weekend(start: datetime, cfg: Dict[str, Any]) -> datetime:
    """
    Apply a weekday-based end-of-week rule.

    Depending on the weekday limit, move the date to Friday or Saturday and
    assign the corresponding hour.
    """
    weekday = start.weekday()

    if weekday < cfg["limit"]:
        target = start + timedelta(days=(4 - weekday))
        return target.replace(hour=cfg["weekday"])

    target = start + timedelta(days=(6 - weekday))
    return target.replace(hour=cfg["weekend"])


def _apply_month_or_quarter(start: datetime, cfg: Dict[str, Any]) -> datetime:
    """
    Apply a monthly or quarterly scheduling rule.

    Monthly rules select the first weekday of the target month.
    Quarterly rules select the last weekday of the previous month.
    """
    period = cfg["period"]
    start_hour = cfg["start_hour"]
    is_quarter = cfg["type"] == "quarter"

    target_month = ((period % 4) * 3 + 1) if is_quarter else period
    target_year = start.year + (target_month <= start.month)

    target = datetime(target_year, target_month, 1, start_hour)

    if is_quarter:
        target -= timedelta(days=1)
        while target.weekday() >= 5:
            target -= timedelta(days=1)
    else:
        while target.weekday() >= 5:
            target += timedelta(days=1)

    return target


def _resolve(description: str) -> Dict[str, Any]:
    """
    Resolve a symbolic rule description into a configuration dictionary.
    """
    if description in RULES:
        return RULES[description]

    if description.endswith("M"):
        return {**RULES["M"], "period": int(description[:-1])}

    if description.startswith("Q"):
        return {**RULES["Q"], "period": int(description[1:])}

    raise ValueError(f"No rule defined for: {description}")


def _dispatch(start: datetime, cfg: Dict[str, Any]) -> datetime:
    """
    Dispatch a rule configuration to its corresponding calculation function.
    """
    rule_type = cfg["type"]

    if rule_type == "offset":
        return _apply_offset(start, cfg)

    if rule_type == "threshold":
        return _apply_threshold(start, cfg)

    if rule_type == "weekend":
        return _apply_weekend(start, cfg)

    if rule_type in ("month", "quarter"):
        return _apply_month_or_quarter(start, cfg)

    raise ValueError(f"Unknown rule type: {rule_type}")


def delivery_date(start_iso: str, description: str) -> str:
    """
    Return a delivery date based on a starting ISO datetime and a rule description.

    Args:
        start_iso: ISO-formatted datetime string representing the starting point.
        description: Symbolic rule description such as 'ASAP', 'EOW', '3M', or 'Q2'.

    Returns:
        ISO-formatted datetime string representing the computed delivery date.
    """
    start = _normalize(datetime.fromisoformat(start_iso))
    cfg = _resolve(description)
    result = _dispatch(start, cfg)
    return result.isoformat()

