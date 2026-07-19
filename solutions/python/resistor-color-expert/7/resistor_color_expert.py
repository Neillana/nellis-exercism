"""Resistance calculator for electrical color-coded resistors.

Provides functionality to decode resistor color bands into their 
respective resistance values and tolerances.
It supports 1, 4, and 5-band color codes.

Constants:
    COLORS: List of color names.
    UNITS: Mapping of divisors to SI-prefixed units.
    TOLERANCES: Mapping of colors to tolerance percentage strings.
"""
COLORS = [
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


def resistor_label(bands: list[str]) -> str:
    """Calculates the resistance and tolerance from color bands.

    Args:
        bands: A list of 1, 4, or 5 color strings representing the resistor bands.

    Returns:
        A string formatted as '{value} {unit} ±{tolerance}' (if applicable).

    Raises:
        ValueError: If the number of bands is not 1, 4, or 5.

    Examples:
        >>> resistor_label(["black"])
        '0 ohms'
        >>> resistor_label(["brown", "black", "brown", "gold"])
        '100 ohms ±5%'
        >>> resistor_label(["red", "red", "orange", "violet"])
        '22 kiloohms ±0.1%'
    """
    if len(bands) not in {1, 4, 5}:
        raise ValueError("Invalid number of bands.")

    digits = bands if len(bands) == 1 else bands[:-2]
    
    base_value = sum(
        COLORS.index(band) * (10 ** exp)
        for exp, band in enumerate(reversed(digits))
    )

    if len(bands) == 1:
        ohm_value = base_value
    else:
        multiplicator = bands[-2]
        ohm_value = base_value * (10 ** COLORS.index(multiplicator))

    tolerance = TOLERANCES.get(bands[-1]) if len(bands) > 1 else None

    base, unit = 1, "ohms"
    for size, name in UNITS.items():
        if ohm_value >= size:
            base, unit = size, name
            break

    result = f"{ohm_value / base:g} {unit}"
    tolerance_suffix = f" \u00b1{tolerance}" if tolerance else ""
    
    return f"{result}{tolerance_suffix}"


    