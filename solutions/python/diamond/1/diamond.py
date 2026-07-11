import string


ALPHABET = string.ascii_uppercase


def rows(letter):
    letter = letter.upper()
    result = []
    letter_index = ALPHABET.index(letter)
    
    for index in range(0, letter_index + 1):
        outer_spaces = " " * (letter_index - index)
        inner_spaces = " " * (2 * index - 1)

        if index == 0:
            row = outer_spaces + ALPHABET[index] + outer_spaces
        else:
            row = (outer_spaces + ALPHABET[index] + inner_spaces + ALPHABET[index] + outer_spaces)
        
        result.append(row)

    return result + result[-2::-1]