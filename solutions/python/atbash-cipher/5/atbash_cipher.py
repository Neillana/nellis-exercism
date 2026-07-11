"""Atbash Cipher

This module provides functionality to encode and decode strings using the 
Atbash cipher, a classic substitution cipher. 

Notes:
    Design Decisions:
    - Separation of Concerns (SoC): The module maintains a strict distinction 
      between encoding and decoding functions. While the underlying 
      transformation is mathematically identical (as Atbash is self-inverse), 
      keeping them separate ensures clarity of intent and extensibility. 
    - Internal Transformation: The _atbash_transform function serves as 
      the core engine, utilizing str.maketrans for efficient character 
      mapping and simultaneous filtering of non-alphabetic characters.
    - Data Integrity: Following principles of database normalization, we 
      avoid "god functions" and conditional flags to ensure that each 
      function has a single, well-defined responsibility. This design 
      protects the module from becoming brittle when future requirements 
      for output formatting (like block grouping) change.

Usage:
    >>> encode("Hello, World!")
    "svool dliow"
    >>> decode("svool dliow")
    "helloworld"
"""
import string


def _atbash_transform(text: str) -> str:
    """Transforms the input text using the Atbash cipher logic.

    This internal helper function creates a mapping between the alphabet and its 
    reverse. It utilizes str.maketrans to simultaneously handle character 
    substitution and the removal of non-alphabetic characters (punctuation and 
    whitespace), as specified by the third argument.

    Args:
        text: The string to be transformed.

    Returns:
        A string containing only the transformed lowercase alphabetic characters.
    """
    text = text.lower()
    alphabet = string.ascii_lowercase
    reversed_alphabet = alphabet[::-1]
    ignore = string.punctuation + string.whitespace
    translation = str.maketrans(alphabet, reversed_alphabet, ignore)
    
    return text.translate(translation)


def encode(plain_text: str) -> str:
    """Encoding a string using the Atbash cipher.
    
    Args:
        plain_text: The string to be encoded.

    Returns:
        The encoded string.
    """
    transformed = _atbash_transform(plain_text)
    chunk_size = 5
    chunks = [
        transformed[offset : offset + chunk_size] 
        for offset in range(0, len(transformed), chunk_size)
    ]
    
    return " ".join(chunks)


def decode(atbash_text: str) -> str:
    """Decodes a string using the Atbash cipher.
    
    Args:
        atbash_text: The string to be decoded.

    Returns:
        The decoded string.
    """
    return _atbash_transform(atbash_text)