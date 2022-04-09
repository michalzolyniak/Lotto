def bad_input(input_to_check, used_numbers, start_number, end_number):
    """
    :param input_to_check:str user input
    :param used_numbers:list with used numbers
    :param start_number: int first number to draw
    :param end_number: int last number to draw
    :return: str error message if occur
    """
    error_message = ""
    try:
        input_number = int(input_to_check)
    except ValueError:
        error_message = f"Input must be hole number from range {start_number} and {end_number}"
        return error_message
    if not start_number <= input_number <= end_number:
        error_message = f"Input must be hole number from range {start_number} and {end_number}"
    elif input_number in used_numbers:
        error_message = f"Number {input_number} has already been chosen."
    return error_message
