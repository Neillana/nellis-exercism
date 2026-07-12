"""
Exercism: Swift Scheduling

A declarative, configuration-driven module to calculate delivery dates based 
on specific scheduling patterns.
"""
from datetime import datetime, timedelta
import re


CONFIGURATION = {
    "FIXED": {
        "NOW":  {"type": "offset", "hours": 2},
        "ASAP": {"type": "threshold", "limit": 13, "early": 17, "late": 13},
        "EOW":  {"type": "weekend", "mid_limit": 3, "early_hour": 17, "late_hour": 20}
    },
    "VARIABLE": {
        "<N>M": {"pattern": r"(\d+)M", "target": "month",   "start_hour": 8},
        "Q<N>": {"pattern": r"Q(\d+)", "target": "quarter", "start_hour": 8}
    }
}


def _handle_fixed(start, config):
    start = start.replace(microsecond=0, second=0, minute=0)
    match config["type"]:
        case "offset":
            return start + timedelta(hours=config["hours"])
        
        case "threshold":
            is_early = start.hour < config["limit"]
            delta = timedelta(days=0 if is_early else 1)
            hour = config["early" if is_early else "late"]
            return (start + delta).replace(hour=hour)
        
        case "weekend":
            is_early = start.weekday() < config["mid_limit"]
            days = (4 if is_early else 6) - start.weekday()
            hour = config["early_hour" if is_early else "late_hour"]
            return (start + timedelta(days=days)).replace(hour=hour)
            

def _handle_variable(start, period_num, config):
    start = start.replace(microsecond=0)
    match config["target"]:
        case "month":
            month, delta, step = period_num, 0, 1
        case "quarter":
            month, delta, step = (period_num % 4) * 3 + 1, -1, -1

    year = start.year + (month <= start.month)
    target = datetime(year, month, 1, config["start_hour"])
    target += timedelta(days=delta)
    
    while target.weekday() >= 5:
        target += timedelta(days=step)
    return target
    

def delivery_date(start, description):
    """
    Calculate the delivery date based on the start datetime and description.
    
    As a rule-based dispatcher, this function first checks for fixed rules
    using direct key lookups. If no fixed rule is found, it then attempts to
    match variable rules using regex patterns defined in the configuration.

    Args:
        start (str): The starting datetime in ISO format.
        description (str): The delivery rule description.

    Returns:
        str: The calculated delivery date in ISO format.

    Raises:
        ValueError: If no matching rule is found for the given description. 

    Examples:
        >>> delivery_date("2024-06-01T10:00:00", "NOW")
        '2024-06-01T12:00:00'
        
        >>> delivery_date("2024-06-01T14:00:00", "ASAP")
        '2024-06-02T13:00:00'
        
        >>> delivery_date("2024-06-01T10:00:00", "EOW")
        '2024-06-04T17:00:00'
        
        >>> delivery_date("2024-06-01T10:00:00", "2M")
        '2024-07-01T08:00:00'
        
        >>> delivery_date("2024-06-01T10:00:00", "Q2")
        '2024-03-31T08:00:00'
    """
    start_dt = datetime.fromisoformat(start)
    
    if description in CONFIGURATION["FIXED"]:
        cfg = CONFIGURATION["FIXED"][description]
        result = _handle_fixed(start_dt, cfg)
    else:
        matches = (
            (int(m.group(1)), cfg) 
            for k, cfg in CONFIGURATION["VARIABLE"].items() 
            if (m := re.fullmatch(cfg["pattern"], description))
        )
        found = next(matches, None)
        if not found:
            raise ValueError(f"No rule defined for: {description}")
        result = _handle_variable(start_dt, *found)

    return result.replace(microsecond=0).isoformat()
    