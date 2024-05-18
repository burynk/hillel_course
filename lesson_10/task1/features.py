"""
External module for pow and some_gen functions
"""


def pow(x: int) -> int:
    """Return the square of x"""
    return x**2


def some_gen(begin: int, end: int, func) -> iter:
    """
    begin: перший елемент послідовності
    end: кількість елементів у послідовності
    func: функція, яка формує значення для послідовності
    """
    yield begin
    for _ in range(end - 1):
        begin = func(begin)
        yield begin
