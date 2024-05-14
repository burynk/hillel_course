"""
Task 7.3. Find the second occurrence of a substring in a given string.
"""

from second_index import second_index

if __name__ == "__main__":
    # Run tests to validate the function

    assert second_index("sims", "s") == 3, "Test1"
    assert second_index("find the river", "e") == 12, "Test2"
    assert second_index("hi", "h") is None, "Test3"
    assert second_index("Hello, hello", "lo") == 10, "Test4"
    print("OK")
