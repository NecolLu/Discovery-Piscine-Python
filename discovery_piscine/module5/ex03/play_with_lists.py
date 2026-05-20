#!/usr/bin/env python3
original_list = [2, 8, 9, 48, 8, 22, -12, 2]
new_set = set()

for num in original_list:
    if num > 5:
        new_set.add(num + 2)  # add() --> adds item arbitrarily to the set (since sets are unodered)

print(original_list)
print(new_set)
