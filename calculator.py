"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:
    input_string = input("Enter your equation :")
    tokenized = input_string.split(" ")

    if tokenized[0] == "q":
        print("Exiting")
        break
    



