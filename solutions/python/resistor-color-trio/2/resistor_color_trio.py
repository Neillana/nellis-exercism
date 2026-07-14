"""Calculates resistor values based on color band codes.

Processes only the first three color bands provided,
ignoring any additional input elements.
"""


BANDS: list[str] = [
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


def label(colors: list[str]) -> str:
    """Convert a list of color bands to a formatted resistance string.

    Args:
        colors: Color labels. Only the first three are used.

    Returns:
        The resistance value with its corresponding SI unit.
    """
    tens, ones, exponent = [BANDS.index(color) for color in colors[:3]]
    value = (tens * 10 + ones) * (10 ** exponent)
    
    unit = None
    match(exponent):
        case 0 | 1:
            result = value
            unit = "ohms"
        case 2 | 3 | 4 | 5:
            result = value // 1000
            unit = "kiloohms"
        case 6 | 7 | 8:
            result = value // 1000000
            unit = "megaohms"
        case 9:
            result = value // 1000000000
            unit = "gigaohms"
    
    phrase = f"{result} {unit}"    
    return phrase
