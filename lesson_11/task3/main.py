"""
Task 11.3. Check if a number is even, without using any division operators.
"""

from is_even import is_even

if __name__ == "__main__":
    assert is_even(2494563894038**2) == True, "Test1"
    assert is_even(1056897**2) == False, "Test2"
    assert is_even(24945638940387**3) == False, "Test3"
