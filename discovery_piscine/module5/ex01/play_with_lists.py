#!/usr/bin/env python3
original_list = [2, 8, 9, 48, 8, 22, -12, 2]
modified_list = []

for num in original_list:
    modified_list.append(num + 2)

# list comprehension method --> modified_list = [num + 2 for num in original_list]

print(f"Original list: {original_list}")
print(f"New list: {modified_list}")
