"""Atbash Cipher

This module provides functionality to encode and decode strings using the 
Atbash cipher, a classic substitution cipher. 

Usage:
    >>> encode("Hello, World!")
    "svool dliow"
    >>> decode("svool dliow")
    "helloworld"
"""
import string


def decode(atbash_text: str) -> str:
    """Decodes a string using the Atbash cipher.
    
    Acts as the core transformation engine, stripping non-alphabetic 
    characters and applying the Atbash mapping.
    """
    text = atbash_text.lower()
    alphabet = string.ascii_lowercase
    reversed_alphabet = alphabet[::-1]
    ignore = string.punctuation + string.whitespace
    translation = str.maketrans(alphabet, reversed_alphabet, ignore)
    
    return text.translate(translation)


def encode(plain_text: str) -> str:
    """Encoding a string using the Atbash cipher.
    
    Transforms the text using the decode logic and adds 5-character 
    grouping for standard Atbash representation.
    """
    transformed = decode(plain_text)
    chunk_size = 5
    chunks = (
        transformed[offset : offset + chunk_size] 
        for offset in range(0, len(transformed), chunk_size)
    )
    
    return " ".join(chunks)