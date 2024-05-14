"""
Module for generating greeting messages
"""


def say_hi(name: str, age: int) -> str:
    """
    Generates a greeting message with the provided name and age.

    :param name: The name of the person (string).
    :param age: The age of the person (int).
    :return: A greeting message including the name and age of the person (formatted string).
    """
    return f"Hi. My name is {name} and I'm {age} years old"
