"""External module for generate_cube_numbers"""


def generate_cube_numbers(end: int) -> iter:
    """
    Generate cube numbers up to a specified endpoint
    :param end: The endpoint up to which cube numbers will be generated
    :return: Cube numbers, up to the 'end'
    """
    for i in range(2, end + 1):
        if i**3 <= end:
            yield i**3
        else:
            return
