"""Binary rebase module.

This module provides functionality to convert numbers between arbitrary
positional numeral systems.

Note:
    These docstrings are my personal learning notes,
    written to explain my implementation steps for future review.
"""


def _get_decimal(input_base: int, digits: list[int]) -> int:
    """Convert positional digits into a standard decimal integer.

    Mathematical Approach (Horner's Method):
    Instead of multiplying each digit by an explicit power of the base 
    (sum(digit * base^index)), this implementation uses Horner's Method: 
    decimal = (...((d_0 * base + d_1) * base + d_2) * ... + d_n).
    
    Why use Horner's Method?
    1. Efficiency: Avoid expensive exponentiation operations (base**index). 
       Each step requires only a single multiplication and an addition.
    2. Performance: The complexity is reduced to O(n), as we only need to 
       iterate through the list once, making it significantly faster for 
       longer digit sequences.
    3. Numerical Stability: By avoiding the calculation of high-magnitude 
       powers, the algorithm is more efficient and handles memory gracefully 
       without creating unnecessary intermediate power values.

    Architectural Note (Single Responsibility Principle):
    This helper function encapsulates both the validation and the decoding 
    of the input digits. It ensures that the core mathematical algorithm 
    never operates on illegal data, keeping the main 'rebase' function 
    free from input-parsing details.
    """
    if not digits:
        return 0
    
    decimal = 0
    
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        decimal = decimal * input_base + digit

    return decimal


def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """Convert a number from an input base to an output base.

    Algorithmic Approach:
    This function utilizes a two-step conversion process:
    1. Input Parsing:
       Uses '_get_decimal' (implemented via Horner's Method) to transform 
       the input list of digits into a decimal integer.
    
    2. Output Encoding (Division-Remainder Method):
       Transforms the resulting decimal integer into the target base:
       - 'divmod()' is used for efficient calculation of remainders and quotients.
       - '.append()' is used to collect remainders, as it avoids the O(n^2) 
         cost of memory-shifting associated with '.insert(0, ...)'.
       - '.reverse()' is applied in-place to the final list, which is 
         more memory-efficient than creating a new copy via the slice 
         operator '[::-1]'.
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
        decimal_value, remainder = divmod(decimal_value, output_base)
        rebased_values.append(remainder)
    rebased_values.reverse()

    return rebased_values
    