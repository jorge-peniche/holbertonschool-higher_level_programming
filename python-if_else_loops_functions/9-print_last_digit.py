#!/usr/bin/python3

def print_last_digit(number):
    last_num = str(number)[-1]
    print(f"{last_num}", end="")
    return last_num


print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
