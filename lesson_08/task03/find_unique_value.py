"""
External module for the find_unique_value() function.
"""


def find_unique_value(some_list: list) -> int:
    """
    Find a unique integer value in a list.
    :param some_list: List of numbers.
    :return: Unique value.
    """
    unique = [i for i in some_list if some_list.count(i) == 1]
    return float(unique[0])
