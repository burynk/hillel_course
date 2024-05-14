"""
External module for the palindrome function
"""
import string


def is_palindrome(text: str) -> bool:
    """
    Check if a string is palindrome, by stripping it and then reversing it.
    :param text: string to be checked
    :return: true if string is palindrome, false otherwise
    """
    stripped = text.translate(str.maketrans('', '', string.punctuation + " ")).lower()
    return stripped[::-1] == stripped
