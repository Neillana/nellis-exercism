"""
Facilities for annotating a garden grid with adjacent flower counts.

Design Notes
------------
This solution intentionally implements a gather-based approach using 
declarative generator expressions. 

While a scatter-based approach is theoretically superior in terms of time 
complexity and performance on large scales, a pure Python implementation 
of scatter introduces significant imperative boilerplate, deeply nested 
loops, and index manipulation that compromises code readability. 

Given the constraints of pure Python and the micro-scale of typical 
Minesweeper boards, readability and expressiveness were prioritized over 
premature optimization. In a production-grade database or large-scale engine, 
this memory-update pattern would instead be offloaded to a lower-level 
language (e.g., C/Rust) or specialized vectorized libraries.
"""


EMPTY = " "
FLOWER = "*"
VALID_FIELDS = {EMPTY, FLOWER}


def _validate_garden(garden: list[str]) -> tuple[int, int]:
    """Validate the garden layout and return height and width.

    Checks if the grid is rectangular and contains only permitted characters
    ('*' for flowers and ' ' for empty spaces).

    Args:
        garden: A list of strings representing the grid layout.

    Returns:
        A tuple of integers containing the (height, width) of the grid.
        Returns (0, 0) if the garden is empty.

    Raises:
        ValueError: If the grid rows are inconsistent in length or if 
            any cell contains an invalid character.
    """
    if not garden:
        return 0, 0
    
    height = len(garden)
    width = len(garden[0])

    for row in garden:
        if len(row) != width:
            raise ValueError("The board is invalid with current input.")
        for cell in row:
            if cell not in VALID_FIELDS:
                raise ValueError("The board is invalid with current input.")
                
    return height, width


def annotate(garden: list[str]) -> list[str]:
    """Annotate a garden grid with flower counts.

    Each empty cell in the grid is replaced by a string representing the 
    number of adjacent flowers. Cells already containing flowers remain 
    unchanged.

    Args:
        garden: A list of strings representing the grid layout, 
            where '*' denotes a flower and ' ' denotes an empty space.

    Returns:
        A list of strings representing the annotated grid, where 
        empty spaces adjacent to flowers are replaced by their counts.
    """
    height, width = _validate_garden(garden)
    if height == 0 or width == 0:
        return garden

    result = []

    for row in range(height):
        current_row = []
        for col in range(width):
            if garden[row][col] == FLOWER:
                current_row.append(FLOWER)
                continue

            count = sum(
                0 <= row + row_shift < height 
                and 0 <= col + col_shift < width 
                and garden[row + row_shift][col + col_shift] == FLOWER
                for row_shift in (-1, 0, 1)
                for col_shift in (-1, 0, 1)
                if row_shift != 0 or col_shift != 0
            )

            current_row.append(str(count) if count > 0 else EMPTY)
        result.append("".join(current_row))

    return result
