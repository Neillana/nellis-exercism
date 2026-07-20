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

    Note:
        Uses pattern matching to extract bands. The base resistance is calculated 
        using a generator expression based on color indices. Multipliers and 
        units are applied dynamically based on the calculated base value.

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
    
    if len(bands) == 1:
        ohm_value = COLORS.index(bands[0])
        return f"{ohm_value} ohms"

    *digits, multiplicator, tolerance = bands
    base_value = sum(
        COLORS.index(digit) * (10 ** int(multiplicator))
        for multiplicator, digit in enumerate(reversed(digits))
    )
    ohm_value = base_value * (10 ** COLORS.index(multiplicator))
    tolerance = TOLERANCES.get(tolerance)

    base, unit = 1, "ohms"
    for size, name in UNITS.items():
        if ohm_value >= size:
            base, unit = size, name
            break

    result = f"{ohm_value / base:g} {unit}"
    tolerance_suffix = f" \u00b1{tolerance}"
    
    return f"{result}{tolerance_suffix}"
    