"""Atbash Cipher

Provides functions to encode and decode text using the Atbash cipher, 
while preserving numeric digits and ignoring non-alphanumeric characters.

Notes on Design Choices:

1. Local Alphabet Variable:
    Using a local variable for the alphabet ensures that the function is 
    self-contained and does not rely on external constants. This makes the 
    function more modular and easier to test in isolation.

2. Transformation Logic:
    The transformation logic is encapsulated in a single function, `_atbash_transform`,
    using `str.maketrans` for efficient character mapping. This approach is more
"""
import string


def _atbash_transform(text: str) -> str:
    """Transformation using a local variable for the alphabet.
    
    Using a local variable for the alphabet ensures that the function
    is self-contained and does not rely on external constants.
    This makes the function more modular and easier to test in isolation.    
    """
    alphabet = string.ascii_lowercase

    transformation = str.maketrans(
        alphabet + string.digits,
        alphabet[::-1] + string.digits,
        string.punctuation + " "
    )
    
    return text.lower().translate(transformation)


def encode(plain_text: str) -> str:
    """Encoding a string using the Atbash cipher.
    Args:
        plain_text: The string to be encoded.

    Returns:
        The encoded string.
    """
    transformed = _atbash_transform(plain_text)
    chunks = [transformed[index:index+5] for index in range(0, len(transformed), 5)]
    
    return " ".join(chunks)


def decode(atbash_text: str) -> str:
    """Decodes a string using the Atbash cipher.
    
    Args:
        atbash_text: The string to be decoded.

    Returns:
        The decoded string.
    """
    return _atbash_transform(atbash_text)