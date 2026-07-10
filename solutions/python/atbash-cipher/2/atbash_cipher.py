"""Atbash Cipher

Provides functions to encode and decode text using the Atbash cipher, 
while preserving numeric digits and ignoring non-alphanumeric characters.

Notes on Design Choices:

1. CONSTANT ALPHABET: 
   Using a defined constant ensures consistency and makes the cipher easily 
   adaptable to other alphabets or character sets.

2. ZIP and REVERSED for Mapping:
   This approach dynamically generates the Atbash mapping at runtime. Compared 
   to hard-coded slicing, this is more expressive, as it directly mirrors the 
   mathematical definition of the cipher (pairing the n-th character with the 
   n-th from the end).
"""
import string


ALPHABET = string.ascii_lowercase
ATBASH_MAP = dict(zip(ALPHABET, reversed(ALPHABET)))


def _atbash_transform(text: str) -> str:
    """Transforms the input text using the Atbash cipher.
    
    Args:
        text: The string to be transformed.

    Returns:
        The transformed string, with all letters replaced by their Atbash     
    """
    result = []

    for char in text.lower():
        if char.isdecimal():
            result.append(char)
        elif char in ATBASH_MAP:
            result.append(ATBASH_MAP[char])
            
    return ''.join(result)

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
    transformed = _atbash_transform(plain_text)

    return ' '.join(transformed[i:i+5] for i in range(0, len(transformed), 5))

def decode(atbash_text: str) -> str:
    """Decodes a string using the Atbash cipher.

    Args:
        atbash_text: The string to be decoded.

    Returns:
        The decoded string.

    Example:
        >>> decode("gvhmt 123")
        'testing 123'
    """
    return _atbash_transform(atbash_text.replace(" ", ""))
