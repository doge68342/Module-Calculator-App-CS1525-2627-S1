from utils import get_user_number

def add(a: float, b: float) -> float:
    """
    Adds two inputs together

    :param a: First number
    :param b: Second number
    :return: The sum of a and b
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Subtracts b from a

    :param a: A number
    :param b: The number to subtract a by
    :return: a subtract b
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    multiplies two inputs together

    :param a: First number
    :param b: Second number
    :return: The product of a and b
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divides two inputs together, if b is zero, prints and error message and does not crash program

    :param a: Divdend
    :param b: Divisor
    :return: Quotient
    """
    try:
        return(a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero, please try different divisor")
        return(divide(a, get_user_number()))