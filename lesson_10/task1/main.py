"""
Task 10.1. Generator function w/ yield
"""

from inspect import isgenerator
from features import some_gen, pow

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, "Test1"
assert list(gen) == [2, 4, 16, 256], "Test2"
print("OK")
