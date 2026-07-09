"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    Parameters:
        record (tuple): A (treasure, coordinate) pair.

    Returns:
        str: The extracted map coordinate.
    """
    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    Parameters:
        coordinate (str): A string map coordinate.

    Returns:
        tuple: The string coordinate split into its individual components.
    """
    # instead of: return (coordinate[0], coordinate[1])
    # direct unpacking = better style:
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, tuple(coordinate_1, coordinate_2), quadrant) trio.

    Returns:
        bool: Do the coordinates match?
    """
    # instead of: return convert_coordinate(azara_record[1]) == rui_record[1]
    # directly unpacking the tuple (no indexes needed then):
    _, azara_coordinates = azara_record
    _, rui_coordoordinates, _ = rui_record
    return convert_coordinate(azara_coordinates) == rui_coordoordinates


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, coordinate, quadrant) trio.

    Returns:
        tuple or str: The combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if compare_records(azara_record, rui_record):
        # use tuple addition
        return azara_record + rui_record
    
    return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    Parameters:
        combined_record_group (tuple): Everything from both participants.

    Returns:
        str: Everything "cleaned", excess coordinates and information are removed.

    Note:
        The return statement is a multi-lined string with items separated by newlines.
        (see HINTS.md for an example).

    """
    report = []

    for treasure, _, location, coord, quadrant in combined_record_group:
        # instead of: cleaned_tuple = (record[0], record[2], record[3], record[4])
        # unpack the tuple using _ for indexes to be left out
        cleaned_tuple = (treasure, location, coord, quadrant)
        report.append(f"{cleaned_tuple}")
            
    return "\n".join(report) + "\n"
