#!/usr/bin/env python3
import sys

if len(sys.argv) == 3:
    str_to_be_searched = sys.argv[2]

    matches = str_to_be_searched.count(sys.argv[1])

    if matches > 0:
        print(matches)
    else:
        print("none")
else:
    print("none")

# The count() method in Python is a built-in tool
# used to find out how many times a specific element appears in a sequence, such as a list, string, or tuple
