from random import sample


def draw_numbers(start, end, quantity):
    """
    :param start: int beginning of range to draw
    :param end: int end of range to draw
    :param quantity: int quantity of numbers to draw
    :return:list of unique drawn numbers from range start to end
    """
    numbers = sample(range(start, end + 1), quantity)
    numbers.sort()
    return numbers
