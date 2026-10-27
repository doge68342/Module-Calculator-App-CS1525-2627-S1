from operations import (
    add,
    subtract,
    multiply,
    divide
)

from utils import (
    get_user_number,
    get_operation
)

while True:
    a = get_user_number()
    operation = get_operation()
    b = get_user_number()

    print("Answer - ", end="")

    if operation == "+":
        print(add(a, b))
    if operation == "-":
        print(subtract(a, b))      
    if operation == "*":
        print(multiply(a, b))
    if operation == "/":
        print(divide(a, b))