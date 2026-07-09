def square(number: int):
    """Compute the number of grains on a given chessboard square.
    
    Squares are numbered 1 through 64 (1-indexed).
    Eeach subsequent square doubles the grains.
    
    Args:
        number: The square number (must be an integer in the range 1..64).
        
    Returns:
        The number of grains on that square.
        
    Raises:
        ValueError: If `number` is not in the range 1..64.
    """
    if not 0 < number < 65:
        raise ValueError("square must be between 1 and 64")
    grains = 2**(number-1)
    return grains


def total():
    return 2**64-1
