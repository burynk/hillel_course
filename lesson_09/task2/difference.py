"""
External module for the difference function
"""


def difference(*args: int | float) -> int | float:
    """
    Calculate the difference between the maximum and minimum values
    from a list of numbers.
    :param args: Any number of integers or floats
    :return: The difference between the maximum and minimum values
    rounded to two decimal places
    """
    if len(args) == 0:
        return 0
    else:
        return round(max(args) - min(args), 2)
