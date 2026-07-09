import math


def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError('Classification is only possible for positive integers.')
    
    if number == 1:
        return 'deficient'

    aliquot = 1
    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            aliquot += i
            complement = number // i
            if complement != i:
                aliquot += complement

    if aliquot == number:
        return 'perfect'
    if aliquot > number:
        return 'abundant'
    return 'deficient'
