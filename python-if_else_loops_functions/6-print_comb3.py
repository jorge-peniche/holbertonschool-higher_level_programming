#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            print(
                "" if i == 0 and j == 1 else ", ",
                "{}{}".format(i, j), sep="", end=""
                )
print('')
