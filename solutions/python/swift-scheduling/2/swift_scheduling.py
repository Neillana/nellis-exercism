"""
Exercism: Swift Scheduling

A declarative, configuration-driven module to calculate delivery dates based 
on specific scheduling patterns.

Notes:
This module employs a YAML-simulated configuration pattern to separate 
business rules from processing logic.

1. YAML-SIMULATED CONFIGURATION:
   The `CONFIG` dictionary acts as a centralized schema. By structuring 
   data like a YAML file, all "Magic Numbers" (thresholds, offsets, 
   time limits) are moved out of the source code. This makes the system 
   easily adjustable without modifying the underlying execution logic.

2. DECLARATIVE DISPATCHER:
   The `delivery_date` function operates as a rule-based dispatcher:
   - Fixed rules use direct key lookups for O(1) performance.
   - Variable rules use regex-based pattern matching defined within 
     the configuration to extract required parameters (e.g., month or quarter).

3. LOGIC HANDLERS:
   Generic, private helper functions (`_handle_fixed`, `_handle_variable`) 
   consume the configuration schema and the start timestamp to perform 
   calculations. This ensures that the code remains purely functional 
   and free of hard-coded constants.

Further Thinking: Scalability & Microservices
---------------------------------------------
This architecture serves as a robust foundation for a microservice in an 
enterprise environment. The decoupling of configuration and logic allows for 
department-specific rule sets:
- Dynamic Configuration: Department leads could manage deadlines via a 
  frontend form, which triggers an automated update of the configuration.
- Validation: Incoming configuration changes can be strictly validated 
  using Pydantic models to ensure schema integrity before persistence.
- Personalization: Through account management and organizational mapping, 
  the service can automatically inject department-specific configuration 
  contexts, enabling personalized scheduling logic at scale.

Flow:
    Input (start, description) 
    -> YAML-Config Schema Lookup 
    -> Dispatcher (Regex/Key Matching) 
    -> Logic Handler (Computation via configuration values) 
    -> Output (ISO formatted datetime)
"""
from datetime import datetime, timedelta
import re


# YAML-SIMULATED CONFIGURATION
CONFIGURATION = {
    "FIXED": {
        "NOW": {
            "type": "offset", 
            "hours": 2
        },
        "ASAP": {
            "type": "threshold", 
            "limit": 13, 
            "early": 17, 
            "late": 13
        },
        "EOW": {
            "type": "weekend", 
            "mid_limit": 3, 
            "early_hour": 17, 
            "late_hour": 20
        }
    },
    "VARIABLE": {
        "<N>M": {
            "pattern": r"(\d+)M",
            "target": "month",
            "start_hour": 8
        },
        "Q<N>": {
            "pattern": r"Q(\d+)",
            "target": "quarter",
            "start_hour": 8
        }
    }
}


def _handle_fixed(start, config):
    """Handle fixed delivery date calculations based on the provided configuration."""
    start = start.replace(microsecond=0)

    match config["type"]:
        case "offset":
            return start + timedelta(hours=config["hours"])

        case "threshold":
            if start.hour < config["limit"]:
                return start.replace(hour=config["early"], minute=0, second=0)
            
            return (start + timedelta(days=1)).replace(hour=config["late"], minute=0, second=0)

        case "weekend":
            if start.weekday() < config["mid_limit"]:
                days = 4 - start.weekday()
                hour = config["early_hour"]
            else:
                days = 6 - start.weekday()
                hour = config["late_hour"]

            return (start + timedelta(days=days)).replace(hour=hour, minute=0, second=0)


def _handle_variable(start, period_num, config):
    """Handle variable delivery date calculations based on the provided configuration."""
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
    result = None

    if description in CONFIGURATION["FIXED"]:
        result = _handle_fixed(start_dt, CONFIGURATION["FIXED"][description])
    else:
        matches = (
            (int(match.group(1)), config)
            for key, config in CONFIGURATION["VARIABLE"].items()
            if (match := re.fullmatch(config["pattern"], description))
        )

        if found := next(matches, None):
            period_num, config = found
            result = _handle_variable(start_dt, period_num, config)

    if result is None:
        raise ValueError(f"No rule defined for: {description}")

    result = result.replace(microsecond=0).isoformat()
    return result

