def is_armstrong_number(number):
    digits = list(str(number))
    count = len(digits)
    result = 0
    for digit in digits:
        result += int(digit)**count
    return result == number