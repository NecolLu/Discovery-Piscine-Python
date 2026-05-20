#!/usr/bin/env python3
import sys

num_params = len(sys.argv) - 1  # -1 to exclude program name

if num_params >= 2:
    while num_params >= 1:
        print(sys.argv[num_params])
        num_params -= 1  # Move one step backward
else:
    print("none")
