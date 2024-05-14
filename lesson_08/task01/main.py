"""
Task 8.1. Increment a number represented by an array.
"""

from lesson_08.task01.add_one import add_one

if __name__ == "__main__":
    # Run tests to validate the function

    assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], "Test1"
    assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test2"
    assert add_one([0]) == [1], "Test3"
    assert add_one([9]) == [1, 0], "Test4"
    print("ОК")
