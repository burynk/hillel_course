"""
Task 10.3. Check if a number is even or odd.
"""

from is_even import is_even

if __name__ == "__main__":
    assert is_even(2) == True, "Test1"
    assert is_even(5) == False, "Test2"
    assert is_even(0) == True, "Test3"
    print("OK")
