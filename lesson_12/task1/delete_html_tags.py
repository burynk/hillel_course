"""External module for deleting HTML tags."""

import codecs
import re

CLEANR = re.compile(r"(<!--.*?-->|<[^>]*>)")


def delete_html_tags(html_file: str, result_file: str = "cleaned.txt") -> None:
    """
    Removes HTML tags and comments from the content of an HTML file and writes the cleaned text to a new file.

    :param html_file:The path to the input HTML file
    :param result_file:The path to the output file where the cleaned text will be saved. Defaults to "cleaned.txt"
    """
    with codecs.open(html_file, "r", "utf-8") as file:
        html = file.read()
    cleantext = re.sub(CLEANR, "", html)
    cleantext = re.sub(r"\n\s*\n", "\n", cleantext).strip()

    with codecs.open(result_file, "w", "utf-8") as file:
        file.write(cleantext)
