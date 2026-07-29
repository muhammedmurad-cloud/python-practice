def safe_sqrt(value): 
    try:
        number = float(value) ** 0.5
    except ValueError:
        return "abc is not a valid number"
    else:
        return number

    # This program demonstrates the use of try, except, and else.
    # It accepts a number from the user, handles invalid input,
    # and calculates the square root if the input is valid.

    