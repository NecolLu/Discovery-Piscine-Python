#!/usr/bin/env python3
usr_input = input("Give me a number: ")

try:
    num = float(usr_input)

    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

except ValueError:
    print("That was not a valid number!")
