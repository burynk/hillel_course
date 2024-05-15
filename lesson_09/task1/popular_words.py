"""
External module for popular words function
"""


def popular_words(text: str, words: list) -> dict:
    """
    Count the occurrences of specific words in a given text.

    :param text: input text
    :param words: list of words
    :return: a dictionary with popular words
    """
    text = text.lower()
    word_list = text.split()

    # Initialize a dictionary
    word_counts = {word: 0 for word in words}

    # Count occurrences of each word in word_list
    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1

    return word_counts
