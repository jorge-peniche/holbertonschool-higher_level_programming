#!/usr/bin/python3
for i in range(26, 0, -1):
    if i % 2 == 0:
        print("{}".format(chr(96 + i)), end="")
    else:
        print("{}".format(chr(64 + i)), end="")
