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
    """Handle fixed delivery date calculations."""
    start = start.replace(microsecond=0)
    match config["type"]:
        case "offset":
            return start + timedelta(hours=config["hours"])
        
        case "threshold":
            if start.hour < config["limit"]:
                return start.replace(hour=config["early"], minute=0, second=0)
            return (start + timedelta(days=1)).replace(
                hour=config["late"], minute=0, second=0
            )
        
        case "weekend":
            if start.weekday() < config["mid_limit"]:
                days = 4 - start.weekday()
                hour = config["early_hour"]
            else:
                days = 6 - start.weekday()
                hour = config["late_hour"]
            return (start + timedelta(days=days)).replace(
                hour=hour, minute=0, second=0
            )


def _handle_variable(start, period_num, config):
    """Handle variable delivery date calculations."""
    start = start.replace(microsecond=0)
    match config["target"]:
        case "month":
            month = period_num
            year = start.year + (month <= start.month)
            target = datetime(year, month, 1, config["start_hour"])
            while target.weekday() >= 5:
                target += timedelta(days=1)
            return target

        case "quarter":
            month = (period_num % 4) * 3 + 1
            year = start.year + (month <= start.month)
            target = datetime(year, month, 1, config["start_hour"]) - timedelta(days=1)
            while target.weekday() >= 5:
                target -= timedelta(days=target.weekday() % 4)
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
    """
    start_date = datetime.fromisoformat(start)
    
    if description in CONFIGURATION["FIXED"]:
        result = _handle_fixed(start_date, CONFIGURATION["FIXED"][description])
    else:
        matches = (
            (int(match.group(1)), config)
            for key, config in CONFIGURATION["VARIABLE"].items()
            if (match := re.fullmatch(config["pattern"], description))
        )
        if found := next(matches, None):
            period_num, config = found
            result = _handle_variable(start_date, period_num, config)
        else:
            raise ValueError(f"No rule defined for: {description}")

    return result.replace(microsecond=0).isoformat()
