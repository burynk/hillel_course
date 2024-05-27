"""External module for is_even"""


def is_even(number: int) -> bool:
    """
    An O(1) solution to check if a number is an even number.
    :param number: number to check
    :return: True if number is even, False otherwise
    """
    return not number & 1
