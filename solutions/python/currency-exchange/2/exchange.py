"""Functions for calculating steps in exchanging currency.
"""

def exchange_money(budget: float, exchange_rate: float) -> float:
    """Calculate estimated value after exchange.

    Parameters:
        budget: The amount of money you are planning to exchange.
        exchange_rate: The unit value of the foreign currency.

    Returns:
        The exchanged value of the foreign currency you can receive.

    Examples:
        >>> exchange_money(127.5, 1.2)
        106.25

        >>> exchange_money(200, 1.10)
        181.82
    """
    return round((budget / exchange_rate), 2)


def get_change(budget: float, exchanging_value: float) -> float:
    """Calculate currency left after an exchange.

    Parameters:
        budget: The amount of money you own.
        exchanging_value: The amount of your money you want to exchange now.

    Returns:
        The amount left of your starting currency after the exchange

    Examples:
        >>> get_change(127.5, 120.0)
        7.5

        >>> get_change(300.75, 150.25)
        150.50
    """
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Calculate the total value of currency at current denomination.

    Parameters:
        denomination: The value of a single unit (bill).
        number_of_bills: The total number of units (bills).

    Returns:
        Calculated value of the units (bills).

    Examples:
        >>> get_value_of_bills(5, 128)
        640

        >>> get_value_of_bills(15.13, 16)
        242
    """
    return int(denomination * number_of_bills)


def get_number_of_bills(amount: float, denomination: int) -> int:
    """Calculate the number of currency units (bills) within the amount.

    Parameters:
        amount: The total starting value.
        denomination: The value of a single unit (bill).

    Returns:
        The number of units (bills) that can be obtained from the amount.

    Examples:
        >>> get_number_of_bills(127.5, 5)
        25

        >>> get_number_of_bills(35.16, 10)
        3
    """
    return amount // denomination


def get_leftover_of_bills(amount: float, denomination: int) -> float:
    """Calculate leftover amount after exchanging into bills.

    Parameters:
        amount: The total starting value.
        denomination: The value of a single unit (bill).

    Returns:
        The amount that is "leftover", given the current denomination.

    Examples:
        >>> get_leftover_of_bills(127.5, 20)
        7.5

        >>> get_leftover_of_bills(153.2, 10)
        3.20
    """
    return round(amount % denomination, 2)


def exchangeable_value(
    budget: float,
    exchange_rate: float,
    spread: int,
    denomination: int
    ) -> int:
    """Calculate the maximum value of the new currency.

    Parameters:
        budget: The amount of your money you are planning to exchange.
        exchange_rate: The unit value of the foreign currency.
        spread: The percentage that is taken as an exchange fee.
        denomination: The value of a single unit (bill).

    Returns:
        The maximum value you can get in the new currency.

    Examples:
        >>> exchangeable_value(127.25, 1.20, 10, 20)
        80

        >>> exchangeable_value(127.25, 1.20, 10, 5)
        95

    Note:
        The currency denomination is a whole number and cannot be sub-divided.
    """
    actual_rate = exchange_rate * (1 + spread / 100)
    actual_exchange = exchange_money(budget, actual_rate)
    bills = get_number_of_bills(actual_exchange, denomination)
    
    return get_value_of_bills(denomination, bills) 
    