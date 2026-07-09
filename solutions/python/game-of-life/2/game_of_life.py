"""Just for me:
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

Basics:
coordinates: matrix[row][col]
horizontal neighbours: row [-1, 0, +1]
vertical neighbours: col [-1, 0, +1]
living_space = height * width of the matrix

ToDo:
- Check if a cell of the input matrix is alive: return matrix[row][col] == 1 -> bool
- Check how many living neighbours a cell has: return neighbours -> int
- Take care about the size of the given matrix (living_space) -> tuple
- Create a new_matrix filled with zeros: new_matrix = [[0] * len(row) for row in matrix]
- Decide if a cell will live or die and get it into the new_matrix: new_matrix[row][col] += 1
- Return the new_matrix

Praise the ones who invented numpy!
May they be covered with gold and live in fortune!
"""

def _size(matrix):
    """Returns the size of a given 2D-matrix
    """
    height = len(matrix)
    width = len(matrix[0])
    return height, width


def _is_alive(matrix, row: int, col: int) -> bool:
    """Returns if a given cell is alive
    """
    return matrix[row][col] == 1


def _count_living_neighbours(matrix, row: int, col: int) -> int:
    """Returns number of living neighbours for a given cell.
    """
    height, width = _size(matrix)
    neighbours = 0

    for row_shift in (-1, 0, +1):
        for col_shift in (-1, 0, +1):
            # ignore the cell itself
            if row_shift == 0 and col_shift == 0:
                continue
        
            neighbour_row_index = row + row_shift
            neighbour_col_index = col + col_shift

            # check if the neighbours are inside the matrix
            if 0 <= neighbour_row_index < height and 0 <= neighbour_col_index < width:
                if matrix[neighbour_row_index][neighbour_col_index] == 1:
                    neighbours += 1

    return neighbours


def tick(matrix):
    """Checks if a cell in a given matrix will life or die and returns the new matrix.
    """
    if not matrix:
        return []
    
    height, width = _size(matrix)
    new_matrix = [[0] * width for height in matrix]

    for row in range(height):
        for col in range(width):
            alive = _is_alive(matrix, row, col)
            neighbours = _count_living_neighbours(matrix, row, col)

            if alive and neighbours in (2, 3):
                new_matrix[row][col] = 1
            elif not alive and neighbours == 3:
                new_matrix[row][col] = 1
            else:
                new_matrix[row][col] = 0

    return new_matrix