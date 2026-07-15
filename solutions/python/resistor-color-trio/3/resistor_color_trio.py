"""Calculates resistor values based on color band codes.

Processes only the first three color bands provided,
ignoring any additional input elements.
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


UNITS = {1000000000: "gigaohms", 1000000: "megaohms", 1000: "kiloohms"}


def label(bands: list[str]) -> str:
    """Convert a list of color bands to a formatted resistance string.

    Args:
        bands: Color labels. Only the first three are used.

    Returns:
        The resistance value with its corresponding SI unit.
    """
    tens, ones, exponent = [COLORS.index(band) for band in bands[:3]]
    value = (tens * 10 + ones) * (10 ** exponent)
    
    for base, unit in UNITS.items():
        if value >= base:
            return f"{value // base} {unit}"
            
    return f"{value} ohms"
