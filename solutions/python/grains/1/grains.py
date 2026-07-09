def square(number: int):
    if not 0 < number < 65:
        raise ValueError("square must be between 1 and 64")
    else:
        grains = 2**(number-1)
        return grains


def total():
    return 2**64-1
