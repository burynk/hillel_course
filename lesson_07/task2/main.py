"""
Task 7.2. Format a string to be title case and end with a full stop.
"""

from correct_sentence import correct_sentence

if __name__ == "__main__":
    # Run tests to validate the function

    assert correct_sentence("greetings, friends") == "Greetings, friends.", "Test1"
    assert correct_sentence("hello") == "Hello.", "Test2"
    assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", "Test3"
    assert correct_sentence("Greetings, friends.") == "Greetings, friends.", "Test4"
    assert correct_sentence("greetings, friends.") == "Greetings, friends.", "Test5"
    print("ОК")
