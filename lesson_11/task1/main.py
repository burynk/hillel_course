"""
Task 11.1. Prime generator
"""

from inspect import isgenerator
from prime_generator import prime_generator

if __name__ == "__main__":

    gen = prime_generator(1)
    assert isgenerator(gen) == True, "Test0"
    assert list(prime_generator(10)) == [2, 3, 5, 7], "Test1"
    assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], "Test2"
    assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], "Test3"
    print("Ok")
