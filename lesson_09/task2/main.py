"""
Task 9.2. Find the difference between two numbers
"""

from difference import difference

if __name__ == "__main__":
    assert difference(1, 2, 3) == 2, "Test1"
    assert difference(5, -5) == 10, "Test2"
    assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, "Test3"
    assert difference() == 0, "Test4"
    print("OK")
