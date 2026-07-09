"""Check whether sentences contain all letters of a configurable alphabet.

Provides a function that normalizes input, filters characters, and verifies
alphabet coverage in a case-insensitive way.
"""
import string

def is_pangram(sentence: str) -> bool:
    """Check whether the sentence contains every letter of the given alphabet.

    The alphabet is defined inside the function and can be replaced to validate
    different writing systems or custom character sets.
    """
    alphabet = set(string.ascii_lowercase)
    letters = {
        letter.lower()
        for letter in sentence
        if letter.lower() in alphabet
    }
    return alphabet <= letters
