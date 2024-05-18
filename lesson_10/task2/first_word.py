""" External module for first_word """

import re


def first_word(text: str) -> str:
    """
    Search for the first word in a given string
    :param text: the string to search
    :return: matched word using regex, skipping punctuation
    """
    return re.search(r"[a-zA-Z']+", text).group(0)
