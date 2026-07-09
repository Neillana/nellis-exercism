def score(x: int, y: int) -> int:
    distance = x*x + y*y
    for radius, points in [(1, 10), (5, 5), (10, 1)]:
        if distance <= radius*radius:
            return points
    return 0
