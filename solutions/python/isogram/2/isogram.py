"""Utility for working with isograms.

This module provides a function that checks whether a word or phrase
contains only unique letters, ignoring case and non-alphabetic characters.
"""
import string

def is_isogram(text: str) -> bool:
    """Return True if the word contains no repeated letters of the given alphabet.

    The function normalizes the input to lower-case, filters out all characters
    that are not part of the chosen alphabet, and checks whether any letter
    appears more than once.
    """
    alphabet = set(string.ascii_lowercase)
    letter_seen = set()
    
    for letter in text.lower():
        if letter in alphabet:
            if letter in letter_seen:
                return False
            letter_seen.add(letter)
            
    return True
