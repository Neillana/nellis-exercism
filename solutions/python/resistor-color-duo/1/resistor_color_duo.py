"""Resistor Color Duo

Maps the first two colors of a given color list
to their concatenated index values.
"""


def value(colors):
    color_list = [
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

    # using generator expression
    result = int("".join(str(color_list.index(color)) for color in colors[:2]))

    return result
