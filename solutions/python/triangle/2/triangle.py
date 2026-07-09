"""
Triangle classification module.

This module provides functions to validate and classify triangles
into three categories based on the lengths of their sides.
"""


def _is_triangle(sides: list[int | float]) -> bool:
    """Validate if the given side lengths can form a valid triangle.

    Sorts the sides so that 'a' is the shortest side
    and 'c' is the longest side.
    This allows the triangle inequality theorem 
    to be verified using a single check (a + b >= c).

    Args:
        sides: Three numerical values representing the sides.

    Returns:
        True if it is a mathematically valid triangle.
    """
    a, b, c = sorted(sides)
    return a > 0 and a + b >= c


def equilateral(sides: list[int | float]) -> bool:
    """Check if the triangle is equilateral.

    A triangle is strictly equilateral if it is valid and all three sides 
    are equal, resulting in exactly 1 unique value.

    Args:
        sides: Three numerical values representing the sides.

    Returns:
        True if the triangle is strictly equilateral.
    """
    return _is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    """Check if the triangle is isosceles.

    A triangle is isosceles if it is valid and has two or more 
    equal sides, resulting 1 or 2 unique values.

    Args:
        sides: Three numerical values representing the sides.

    Returns:
        True if the triangle is isosceles.
    """
    return _is_triangle(sides) and len(set(sides)) <= 2


def scalene(sides):
    """Check if the triangle is scalene.

    A triangle is scalene if it is valid and all three sides have 
    different lengths, resulting in exactly 3 unique values.

    Args:
        sides: Three numerical values representing the sides.

    Returns:
        True if the triangle is scalene.
    """
    return _is_triangle(sides) and len(set(sides)) == 3
