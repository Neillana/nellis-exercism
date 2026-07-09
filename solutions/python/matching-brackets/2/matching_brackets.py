"""Module to verify bracket pairing in text.

Provides functionality to check if all pairs of round, curly, 
and square brackets are correctly matched and nested.
"""


def is_paired(input_string: str) -> bool:
    """Iterates through a given string and matches found brackets.

    Uses a stack-based algorithm to verify if all pairs of brackets
    `()`, `{}`, and `[]` are correctly nested and closed in the correct order.
    Non-bracket characters are safely ignored.

    Args:
        input_string: The string containing the characters and brackets to check.

    Returns:
        True if all brackets are properly matched and closed, False otherwise.

    Examples:
        >>> is_paired("[Text (with matching brackets)]")
        True
        >>> is_paired("(Text [with not matching) brackets]")
        False
    """
    opening = ["(", "{", "["]
    closing = [")", "}", "]"]
    found_brackets = []
    
    for char in input_string:
        if char in opening:
            found_brackets.append(char)
        if char in closing:
            index = closing.index(char)
            expected_opening = opening[index]

            if not found_brackets or found_brackets.pop() != expected_opening:
                return False
                
    return len(found_brackets) == 0
