"""
Provides Caesar cipher functionality for encoding text.
"""

def rotate(text: str, key: int) -> str:
    """
    Converts the given text using the Caesar cipher.

    Parameters:
        text: The text to encode.
        key: The rotation amount applied to alphabetic characters.

    Returns:
        The encoded text where alphabetic characters are shifted by the given key,
        while all non-alphabetic characters (including whitespace and punctuation)
        remain unchanged.
    """
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ceasar_text = []

    for digit in text:
        if digit.isalpha():
            alphabet = alphabet_lower if digit.islower() else alphabet_upper
            index = alphabet.index(digit)
            rotation = (index + key) % 26
            ceasar_text.append(alphabet[rotation])
        else:
            ceasar_text.append(digit)
    
    return ''.join(ceasar_text)
