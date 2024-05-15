"""
External module for the increment function
"""


def add_one(some_list: list[int]) -> list[int]:
    """
    Increment a number represented as a list of digits by one and return the result as a list of digits.
    :param some_list: List of integers representing a number
    :return: List of integers representing the incremented number
    """
    number = "".join(map(str, some_list))
    number = str(int(number) + 1)
    result = list(map(int, number))
    return result
