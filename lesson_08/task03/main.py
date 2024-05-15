"""
Task 8.3. Find a unique number
"""

from find_unique_value import find_unique_value

if __name__ == "__main__":
    # Run tests to validate the function

    assert find_unique_value([1, 2, 1, 1]) == 2, "Test1"
    assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, "Test2"
    assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, "Test3"
    print("ОК")
