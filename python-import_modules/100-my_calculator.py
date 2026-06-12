#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    file = argv.pop(0)

    if len(argv) != 3:
        print(f"Usage: {file} <a> <operator> <b>")
        exit(1)

    a = int(argv[0])
    b = int(argv[2])

    if argv[1] == "+":
        print(f"{a} + {b} = {add(a, b)}")
    elif argv[1] == "-":
        print(f"{a} - {b} = {sub(a, b)}")
    elif argv[1] == "*":
        print(f"{a} * {b} = {mul(a, b)}")
    elif argv[1] == "/":
        print(f"{a} / {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
