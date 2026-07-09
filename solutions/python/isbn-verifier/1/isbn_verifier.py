def is_valid(isbn: str) -> bool:
    """Validate whether a given string represents a correct ISBN-10.

    The function normalizes the input by removing dashes and converting the
    check character to upper-case. It then verifies the structural format
    and computes the weighted checksum according to the ISBN-10 specification.
    Returns True if the checksum is divisible by 11, otherwise False.
    """
    # Normalize user input
    isbn = isbn.replace("-", "").upper()

    # Verify that the ISBN has exactly 10 characters
    if len(isbn) != 10:
        return False

    # Validate the structural format of an ISBN-10
    if not (isbn[:9]).isdigit() or isbn[-1] not in "0123456789X":
        return False

    # Convert characters to numeric values
    digits = [int(number) for number in isbn[:9]]
    # if "X" is the last digit, it counts as 10
    last_digit = 10 if isbn[-1] == "X" else int(isbn[-1])
    digits.append(last_digit)

    # Mapping digits and weights (checksum)
    total = sum(
        digit * weight for digit,
        weight in zip(digits, range(10, 0, -1))
    )

    return total % 11 == 0
    