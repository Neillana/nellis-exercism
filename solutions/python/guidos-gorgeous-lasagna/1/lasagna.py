"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    elapsed = EXPECTED_BAKE_TIME - elapsed_bake_time
    if elapsed > 0:
        return elapsed
    else:
        return "Ready to eat!"


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    Parameters:
        number_of_layers (int): The number of layers of the lasagna.

    Returns:
        int: The preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers of the lasagna as
    an argument and returns how many minutes the preparation takes
    based on the `PREPARATION_TIME` per layer.
    """
    preparation = PREPARATION_TIME * number_of_layers
    return preparation


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time.

    Parameters:
        number_of_layers (int): The number of layers of the lasagna.
        elapsed_bake_time (int): The time the lasagne has spent in the oven.

    Returns:
        int: The time (in minutes) spent in the kitchen.

    Function that takes the number of layers of the lasagna and the elapsed bake time as
    arguments and returns how many minutes have been spent in the kitchen.
    """
    time_spent = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return time_spent


