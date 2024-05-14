"""
Task 7.1. Function to introduce someone with specified name and age
"""

from say_hi import say_hi

if __name__ == "__main__":
    # Run tests to validate the function
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "Test1"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Test2"
    print("ОК")
