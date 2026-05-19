#!/usr/bin/env python3
import math

usr_input = input("Give me a number: ")

try:
    num = float(usr_input)
    result = math.ceil(num)
    print(result)

except ValueError:
    print("Please enter a valid number.")
