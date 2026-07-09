"""Functions for tracking poker hands and assorted card tasks.
"""


def _average(cards: list) -> float:
    """Auxiliary function to calculate average of given cards.
    """
    return sum(cards) / len(cards)


def get_rounds(number: int) -> list:
    """Create a list containing the current and next two round numbers.
    """
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: list, rounds_2: list) -> list:
    """Concatenate two lists of round numbers.
    """
    return list(rounds_1 + rounds_2)


def list_contains_round(rounds: list, number: int) -> bool:
    """Check if the list of rounds contains the specified number.
    """
    return number in rounds


def card_average(hand: list) -> float:
    """Calculate and returns the average card value from the list.
    """
    return _average(hand)


def approx_average_is_average(hand: list) -> bool:
    """Return if the average of first and last card or the 'middle' card equals calculated average.
    """
    average = _average(hand)
    average_first_last = _average([hand[0], hand[-1]])
    median = hand[len(hand) // 2]
    
    return average_first_last == average or median == average


def average_even_is_average_odd(hand: list) -> bool:
    """Return if the average of even indexed card values equals the average of odd indexed card values.
    """
    even_cards = hand[::2]
    odd_cards = hand[1::2]
    
    return _average(even_cards) == _average(odd_cards)


def maybe_double_last(hand: list) -> list:
    """Multiply a Jack card value in the last index position by 2.
    """
    if hand[-1] == 11:
            hand[-1] = 22
            return hand
    return hand
