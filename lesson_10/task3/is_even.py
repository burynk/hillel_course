"""External module for is_even."""


def is_even(digit: int) -> bool:
    """
    Return True if the given number is an even number.
    :param digit: integer value.
    :return: true if number is even, false otherwise.
    """
    return digit % 2 == 0
