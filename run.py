from functions.bad_input import bad_input
from functions.draw_numbers import draw_numbers
from functions.hit_numbers import hit_numbers

if __name__ == '__main__':
    FIRST_DRAW_NUMBER = 1
    LAST_DRAW_NUMBER = 49
    AMOUNT_NUMBERS = 6
    MIN_WIN_QUANTITY = 3
    drawn_numbers = draw_numbers(FIRST_DRAW_NUMBER, LAST_DRAW_NUMBER, AMOUNT_NUMBERS)
    user_numbers = []
    while True:
        if user_numbers:
            print(f"Chosen numbers {', '.join(str(number) for number in user_numbers)}")
        user_input = input(
            f"Enter {len(user_numbers) + 1}/{AMOUNT_NUMBERS} number from range {FIRST_DRAW_NUMBER} and {LAST_DRAW_NUMBER}:")
        bad_input_message = bad_input(user_input, user_numbers, FIRST_DRAW_NUMBER, LAST_DRAW_NUMBER)
        if bad_input_message != "":
            print(bad_input_message)
            continue
        user_numbers.append(int(user_input))
        user_numbers.sort()
        if len(user_numbers) < 6:
            continue
        user_numbers.sort()
        guessing_numbers = hit_numbers(drawn_numbers, user_numbers)
        print(f"You have chosen the following numbers: {', '.join(str(number) for number in user_numbers)}")
        print(f"The drawn numbers are: {', '.join(str(number) for number in drawn_numbers)}")
        if len(guessing_numbers) >= MIN_WIN_QUANTITY:
            print(f"Congratulations you won. You hit {len(guessing_numbers)} of {AMOUNT_NUMBERS} numbers")
            print(f"Your wining numbers are {', '.join(str(number) for number in guessing_numbers)}")
        else:
            if guessing_numbers:
                print(f"Sorry you did not win. You hit only {len(guessing_numbers)} of {AMOUNT_NUMBERS} numbers")
            else:
                print("Sorry you did not win. Not any of your numbers were drawn")
        break
