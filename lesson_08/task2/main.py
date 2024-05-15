"""
Task 8.2. Check if a string is a palindrome.
"""

from is_palindrome import is_palindrome

if __name__ == "__main__":
    # Run tests to validate the function
    assert is_palindrome("A man, a plan, a canal: Panama") == True, "Test1"
    assert is_palindrome("0P") == False, "Test2"
    assert is_palindrome("a.") == True, "Test3"
    assert is_palindrome("aurora") == False, "Test4"
    print("OK")
