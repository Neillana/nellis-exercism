"""
Provides functions to compare two lists and classify their relationship
as EQUAL, UNEQUAL, SUBLIST or SUPERLIST.
"""

# Relationship constants
EQUAL = 0
UNEQUAL = 1
# Subvalues of unequal:
SUBLIST = 11
SUPERLIST = 12


def _is_sublist(shorter_list: list, longer_list: list) -> bool:
    """Return True if shorter_list occurs as a contiguous slice within longer_list.
    """
    length = len(shorter_list)

    if length == 0:
        return True
    
    return any(
        longer_list[index:index+length] == shorter_list
        for index in range(len(longer_list) - length + 1)
    )

    
def sublist(list1: list, list2: list) -> int:
    """Compares two given lists and returns their relationship."""
    if list1 != list2:
        if len(list1) < len(list2):
            if _is_sublist(list1, list2):
                return SUBLIST
        else:
            if _is_sublist(list2, list1):
                return SUPERLIST
            
        return UNEQUAL
    
    return EQUAL
