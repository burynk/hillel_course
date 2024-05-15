"""
External module for the common_elements function
"""


def common_elements():
    """
    Function to find common elements between two lists
    :return: list of common elements
    """
    x = range(0, 100, 3)
    y = range(0, 100, 5)
    common = set(x) & set(y)
    return common
