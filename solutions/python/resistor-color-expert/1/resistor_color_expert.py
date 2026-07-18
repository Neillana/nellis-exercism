"""Calculate and format resistor values based on color bands.

Decode resistor color bands (1, 4, or 5 bands) into their corresponding 
resistance values in ohms, kiloohms, megaohms, or gigaohms, along with 
their associated tolerance values where applicable.
"""


COLORS: list[str] = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]


UNITS = {
    1000000000: "gigaohms",
    1000000: "megaohms",
    1000: "kiloohms",
    }


TOLERANCES = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}


def resistor_label(colors: list[str]) -> str:
    """Calculate the total resistance and tolerance from color bands.

    Args:
        colors: A list containing 1, 4, or 5 resistor color names.

    Returns:
        The formatted resistance value with its unit and tolerance.

    Raises:
        ValueError: If the number of color bands is not 1, 4, or 5.
    """    
    def value(color: str) -> int:
        """Look up the numeric index value of a specific color."""
        return COLORS.index(color)

    match colors:
        case [color]:
            ohm_value = value(color)
            tolerance = None

        case [band1, band2, multiplier, tolerance_band]:
            base_value = value(band1) * 10 + value(band2)
            ohm_value = base_value * (10 ** value(multiplier))
            tolerance = TOLERANCES[tolerance_band]

        case [band1, band2, band3, multiplier, tolerance_band]:
            base_value = value(band1) * 100 + value(band2) * 10 + value(band3)
            ohm_value = base_value * (10 ** value(multiplier))
            tolerance = TOLERANCES[tolerance_band]
            
        case _:
            raise ValueError("Invalid number of bands.")

    result = ""    
    for base, unit in UNITS.items():
        if ohm_value >= base:
            # Uses General formatting (:g): auto-selects standard or scientific
            # notation for the most compact view and drops trailing zeros.
            result = f"{ohm_value / base:g} {unit}"
            break
        else:
            result = f"{ohm_value} ohms"

    tolerance_suffix = f" \u00b1{tolerance}" if tolerance else ""
    return f"{result}{tolerance_suffix}"
    