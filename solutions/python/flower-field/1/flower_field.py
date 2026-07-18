"""
Annotate empty spaces in a garden grid with adjacent flower counts.

Process a rectangular board (garden matrix) and replace empty cells with the
number of horizontally, vertically, and diagonally adjacent flowers ("*"). 
Validate the structural consistency and character integrity of the input 
grid before processing.
"""


def _size(garden: list) -> tuple:
    """Return the height and width of a garden matrix."""
    height = len(garden)
    width = len(garden[0]) if height > 0 else 0
    return height, width


def _has_flower(garden: list, row: int, col: int) -> bool:
    """Check if a specific cell contains a flower ("*")."""
    return garden[row][col] == "*"


def _count_neighbours(
        garden: list,
        row: int,
        col: int,
        height: int,
        width: int,
    ) -> str:
    """Count how many of the 8 surrounding cells are planted.

    Implementation Details:
    Uses coordinate shifts (-1, 0, 1) to check the 3x3 neighborhood.
    It explicitly skips the center cell itself (shift 0, 0) and
    ensures that all checked indices stay strictly within the bounds
    of the matrix to prevent IndexError.
    """
    neighbours = 0

    for row_shift in (-1, 0, 1):
        for col_shift in (-1, 0, 1):
            if row_shift == 0 and col_shift == 0:
                continue

            n_row = row + row_shift
            n_col = col + col_shift

            if 0 <= n_row < height and 0 <= n_col < width:
                if garden[n_row][n_col] == "*":
                    neighbours += 1

    return str(neighbours) if neighbours > 0 else " "


def annotate(garden):
    """
    Replace empty spaces in a garden grid with the count of adjacent flowers.

    Args:
        garden: List of strings representing the garden grid.

    Returns:
        List of strings with counts of adjacent flowers. 
        Returns an empty list if the input is empty.

    Raises:
        ValueError: If row lengths are inconsistent or invalid characters 
            are present.
    """
    if not garden:
        return garden
    
    width = len(garden[0])
    valid_chars = {" ", "*"}
    
    for row in garden:
        if len(row) != width:
            raise ValueError("The board is invalid with current input.")
            
        for cell in row:
            if cell not in valid_chars:
                raise ValueError("The board is invalid with current input.")
    
    
    height, width = _size(garden)
    garden_matrix = [[" "] * width for _ in garden]

    for row in range(height):
        for col in range(width):
            flower = _has_flower(garden, row, col)
            neighbours = _count_neighbours(
                garden, row, col, height, width
            )

            if not flower:
                garden_matrix[row][col] = neighbours
            else:
                garden_matrix[row][col] = "*"
    
    return ["".join(row) for row in garden_matrix]
