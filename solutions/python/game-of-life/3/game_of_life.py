"""Conway's Game of Life.

Note: These docstrings are my personal learning and mentoring notes,
written to explain my implementation steps for future review.

Praise the ones who invented numpy!
May they be covered with gold and live in fortune!
"""


def _size(matrix: list[list[int]]) -> tuple[int, int]:
    """Return the height and width of a given 2D matrix."""
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    return height, width


def _is_alive(matrix: list[list[int]], row: int, col: int) -> bool:
    """Check if a specific cell is currently alive (1)."""
    return matrix[row][col] == 1


def _count_living_neighbours(
    matrix: list[list[int]],
    row: int,
    col: int,
    height: int,
    width: int,
) -> int:
    """Count how many of the 8 surrounding cells are alive.

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

            # Check boundaries and cell status
            if 0 <= n_row < height and 0 <= n_col < width:
                if matrix[n_row][n_col] == 1:
                    neighbours += 1

    return neighbours


def tick(matrix: list[list[int]]) -> list[list[int]]:
    """Advance the Game of Life matrix by one generation (tick).

    Implementation Details:
    1. Create a snapshot of the matrix dimensions.
    2. Initialize a new matrix with zeros to prevent changing cells
       while we are still counting their neighbors (state isolation).
    3. Apply the rules of life/death based on the neighbor count
       and populate the new matrix.
    """
    if not matrix or not matrix[0]:
        return []

    height, width = _size(matrix)
    # FIX: Use '_' instead of 'height' to prevent variable overriding
    new_matrix = [[0] * width for _ in matrix]

    for row in range(height):
        for col in range(width):
            alive = _is_alive(matrix, row, col)
            # FIX: Pass height/width directly for better performance
            neighbours = _count_living_neighbours(
                matrix, row, col, height, width
            )

            # Apply Conway's rules
            if alive and neighbours in (2, 3):
                new_matrix[row][col] = 1
            elif not alive and neighbours == 3:
                new_matrix[row][col] = 1
            else:
                new_matrix[row][col] = 0

    return new_matrix
