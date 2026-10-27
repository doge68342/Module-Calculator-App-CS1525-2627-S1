def get_user_number() -> float:
    """
    Uses input() to get user input and returns it as a float and tries again if input cannot be converted into a float

    :return: user input as a float
    """
    user_input = input("Numerical input - ")

    try:
        float_user_input = float(user_input)
    except ValueError:
        print("Could not convert user input into float, please try again")
        return get_user_number()

    return float_user_input

def get_operation() -> str:
    """
    Uses input() to get user input and returns it if it is a mathematical symbol (+, -, *, or /)

    :return: mathematical symbol of input
    """
    user_input = input("Operation input - ")

    if user_input == "+" or user_input == "-" or user_input == "*" or user_input == "/":
        return user_input
    else:
        print("Invalid operation try +, -, *, or /")
        return get_operation()