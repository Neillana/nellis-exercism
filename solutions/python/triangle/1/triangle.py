def _is_triangle(sides):
    a, b, c = sides
    return min(a, b, c) > 0 and (a + b >= c and a + c >= b and b + c >= a)


def equilateral(sides):
    a, b, c = sides
    return _is_triangle(sides) and a == b == c


def isosceles(sides):
    a, b, c = sides
    return _is_triangle(sides) and ((a == b) or (a == c) or (b == c))


def scalene(sides):
    a, b, c = sides
    return _is_triangle(sides) and (a != b and a != c and b != c)
