#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv.pop(0)
    addition = 0
    for i in range(len(argv)):
        addition += int(argv[i])
    print(addition)
