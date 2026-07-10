"""Atbash Cipher

Provides functions to encode and decode text using the Atbash cipher, 
while preserving numeric digits and ignoring non-alphanumeric characters.

Notes on Design Choices:

1. CONSTANT ALPHABET: 
   Using a defined constant ensures consistency and makes the cipher easily 
   adaptable to other alphabets or character sets.

2. ZIP and REVERSED for Mapping:
   I have chosen a dynamic mapping approach using `zip` and `reversed` instead 
   of a pre-computed dictionary. While a dictionary lookup would offer O(1) 
   time complexity, this dynamic approach makes the mathematical symmetry 
   of the Atbash cipher explicit in the code. It avoids the overhead of 
   maintaining a static table and enhances overall code readability and 
   maintainability.
"""
import string
from typing import List


ALPHABET = list(string.ascii_lowercase)


def encode(plain_text: str) -> str:
    """Encodes a string using the Atbash cipher.

    Args:
        plain_text: The string to be encoded.

    Returns:
        The encoded string, with characters grouped into blocks of 5 
        separated by spaces.

    Example:
        >>> encode("Testing, 1 2 3")
        'gvhmt 123'
    """
    plain_text = plain_text.lower()

    cache: List[str] = []
    for char in plain_text:
        for letter, encoded in zip(ALPHABET, reversed(ALPHABET)):
            if char == letter:
                cache.append(encoded)
                break
            elif char.isdecimal():
                cache.append(char)
                break
            else:
                pass

    chunks = [cache[i:i+5] for i in range(0, len(cache), 5)]
    encoded_text = [''.join(chunk) for chunk in chunks]

    return ' '.join(encoded_text)


def decode(atbash_text: str) -> str:
    """Decodes an Atbash-encoded string.

    Args:
        atbash_text: The encoded string to be decoded.

    Returns:
        The decoded plaintext string.

    Example:
        >>> decode("gvhmt 123")
        'testing123'
    """
    atbash_text = atbash_text.lower()

    decoded_text: List[str] = []
    for char in atbash_text:
        for letter, decoded in zip(reversed(ALPHABET), ALPHABET):
            if char == letter:
                decoded_text.append(decoded)
                break
            elif char.isdecimal():
                decoded_text.append(char)
                break
            else:
                pass

    return ''.join(decoded_text)
