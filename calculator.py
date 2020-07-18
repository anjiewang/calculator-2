"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:
    input_string = input("Enter your equation: ")
    tokenized = input_string.split(" ")
    if tokenized[0] == "q":
        print("Exiting")
        break
    else:
        num1 = float(tokenized[1])
        num2 = float(tokenized[2])
        if tokenized[0] == "+":
            print(add(num1, num2))
        elif tokenized[0] == "-":
            print(subtract(num1, num2))
        elif tokenized[0] == "*":
            print(multiply(num1, num2))
        elif tokenized[0] == "/":
            print(divide(num1, num2))
        elif tokenized[0] == "square":
            print(square(num1))
        elif tokenized[0] == "cube":
            print(cube(num1))
        elif tokenized[0] == "power":
            print(power(num1, num2))
        elif tokenized[0] == "mod":
            print(mod(num1, num2))





