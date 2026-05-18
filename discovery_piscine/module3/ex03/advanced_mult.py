#!/usr/bin/env python3
table_num = 0

# Outer loop (iterates through tables from 0 to 10)
while table_num <= 10:
    print(f"Table of {table_num}:", end="")

    multiplier = 0
    # Inner loop (calculates and prints products from 0 to 10)
    while multiplier <= 10:
        product = table_num * multiplier
        print(f" {product}", end="")
        multiplier += 1

    print()
    table_num += 1
