"""
External module for the second_index function
"""


def correct_sentence(text: str) -> str:
    """
    Corrects a given text so that each sentence starts with a capital letter and ends with a period.

    :param text: The input text containing sentences.
    :return: The corrected text with proper capitalization and punctuation.
    """
    # Split the string into a list, removing dots and spaces
    textlist = text.split(". ")
    for i in range(len(textlist)):
        # Capitalize every item (sentence)
        textlist[i] = textlist[i].capitalize()
        # Add a full stop if there isn't one already:
        if not textlist[i].endswith("."):
            textlist[i] += "."
    # Join all the items into a single string
    return " ".join(textlist)
