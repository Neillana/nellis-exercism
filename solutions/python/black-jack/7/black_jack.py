"""Utility functions for scoring and evaluating blackjack hands.
"""

MIN_NUMERIC_CARD = 2
MAX_NUMERIC_CARD = 10
SPECIAL_CARD_VALUES = {'J': 10, 'Q': 10, 'K': 10, 'A': 1}


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.
    """
    if card in SPECIAL_CARD_VALUES:
        return SPECIAL_CARD_VALUES[card]
    
    if card.isdigit():
        value = int(card)
        if MIN_NUMERIC_CARD <= value <= MAX_NUMERIC_CARD:
            return value
            
    raise ValueError(f"Invalid card value: '{card}'")


def higher_card(card_one: str, card_two: str) -> str | tuple[str, str]:
    """Return the higher-valued card, or both if equal.
    """
    if value_of_card(card_one) == value_of_card(card_two):
        return (card_one, card_two)
    return max((card_one, card_two), key=value_of_card)


def value_of_ace(card_one: str, card_two: str) -> int:
    """Return the optimal value (1 or 11) for an upcoming ace.
    """
    total = value_of_card(card_one) + value_of_card(card_two)

    if 'A' in (card_one, card_two) or total > 10:
        return 1
    return 11


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.
    """
    total = value_of_card(card_one) + value_of_card(card_two)
    
    return 'A' in (card_one, card_two) and total == 11


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Return True if the two cards can be split into a pair.
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Return True if the hand qualifies for a double-down bet.
    """
    return value_of_card(card_one) + value_of_card(card_two) in {9, 10, 11}
