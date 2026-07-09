"""Binary rebase module.

This module provides functionality to convert numbers between arbitrary
positional numeral systems.

Note:
    These docstrings are my personal learning notes,
    written to explain my implementation steps for future review.
"""


def _get_decimal(input_base: int, digits: list[int]) -> int:
    """Convert positional digits into a standard decimal integer.

    Mathematical Approach:
    Uses positional weighting from right to left. By reversing the
    digits list, the index directly corresponds to the power of the
    base (index 0 is base^0, index 1 is base^1, etc.). The decimal
    value is calculated using the formula:
    sum(digit * (input_base ** index)).

    Architectural Note (Single Responsibility Principle):
    This helper function encapsulates both the validation and the
    decoding of the input digits. It ensures that the core mathematical
    algorithm never operates on illegal data, keeping the main 'rebase'
    function free from input-parsing details.
    """
    if any(digit < 0 or digit >= input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
        
    if not digits:
        return 0
    
    decimal = 0
    
    for index, digit in enumerate(reversed(digits)):
        decimal += digit * (input_base ** index)

    return decimal


def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """Convert a number from an input base to an output base.

    Algorithmic Approach (The Remainder / Division Method):
    1. Validate structural system boundaries (the bases themselves).
    2. Delegate input decoding and digit validation to the private
       '_get_decimal' helper.
    3. Encode the resulting decimal value into the target base using
       successive division:
       - The modulo operator (%) extracts the remainder (the next digit).
       - '.append(remainder)' adds each digit to the end of the list.
         This is more efficient than '.insert(0, ...)' because it
         avoids shifting all existing elements in memory every time.
       - Integer division (//=) reduces the decimal value until it
         reaches zero.
    4. Reverse the accumulated list using the slice operator ([::-1])
       to establish the correct positional order (from bottom to top).
    """
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
      
    decimal_value = _get_decimal(input_base, digits)

    if decimal_value == 0:
        return [0]

    rebased_values = []
    
    while decimal_value > 0:
        remainder = decimal_value % output_base
        rebased_values.append(remainder)
        decimal_value //= output_base

    return rebased_values[::-1]
    