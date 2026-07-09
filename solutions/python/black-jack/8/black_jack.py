"""Utility functions for scoring and evaluating blackjack hands.

Note:
    This solution uses constant-based rule definitions to avoid
    "magic numbers" throughout the logic. By centralizing values
    like THRESHOLD or DOUBLE_DOWN in a configuration-style block,
    the game's rules remain flexible. This makes it easy to adjust
    parameters or implement rule variations (e.g., changing
    card values or modifying deck mechanics) without having to touch
    the core function logic.
"""


SPECIAL_CARDS = {'J': 10, 'Q': 10, 'K': 10}
NUMERIC_CARDS = {2, 3, 4, 5, 6, 7, 8, 9, 10}
ACE = (1, 11)
THRESHOLD = 10
BLACKJACK = 21
DOUBLE_DOWN = {9, 10, 11}


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.
    """
    if card in SPECIAL_CARDS:
        return SPECIAL_CARDS[card]

    if card == 'A':
        return ACE[0]
    
    if card.isdigit():
        if (value := int(card)) in NUMERIC_CARDS:
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

    if 'A' in (card_one, card_two) or total > THRESHOLD:
        return ACE[0]
        
    return ACE[1]


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.
    """
    total = value_of_card(card_one) + value_of_card(card_two)
    
    return 'A' in (card_one, card_two) and total + THRESHOLD == BLACKJACK


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Return True if the two cards can be split into a pair.
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Return True if the hand qualifies for a double-down bet.
    """
    total = value_of_card(card_one) + value_of_card(card_two)
    
    return total in DOUBLE_DOWN
