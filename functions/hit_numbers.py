def hit_numbers(numbers_to_check, in_numbers):
    """
    :param numbers_to_check:list of numbers to check
    :param in_numbers: list to check in
    :return list of numbers from numbers_to_check exist in list in_numbers
    """
    existing_numbers = [number for number in numbers_to_check if number in in_numbers]
    return existing_numbers
