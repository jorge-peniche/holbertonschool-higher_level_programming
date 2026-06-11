#!/usr/bin/python3

def print_last_digit(number):
    if isinstance(number, int):
        last_num = str(number)[-1]
    print(f"{last_num}", end="")
    return last_num
