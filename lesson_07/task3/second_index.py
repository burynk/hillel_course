"""
External module for the second_index function
"""


def second_index(text: str, some_str: str) -> int | None:
    """
    Find the second index of a given substring.
    :param text: The text to be searched.
    :param some_str: The string to be searched.
    :return: The second index of the given substring, or `None` if it is not found.
    """
    first_occurrence = text.find(some_str)
    second_occurrence = text.find(some_str, first_occurrence + 1)
    return second_occurrence if second_occurrence >= 0 else None
