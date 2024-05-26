"""External module for prime_generator"""


def prime_generator(end: int) -> iter:
    """
    Generate prime numbers up to the specified end value
    :param end: The upper limit (inclusive) for generating prime numbers
    :return: An iterator yielding prime numbers
    """

    def is_prime(n: int) -> bool:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    for i in range(2, end + 1):
        if is_prime(i):
            yield i
