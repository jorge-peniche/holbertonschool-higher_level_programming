#!/usr/bin/python3
def uppercase(str_in):
    result = ""
    for i in str_in:
        if 97 <= ord(i) <= 122:
            result += chr(ord(i)-32)
        else:
            result += str(i)
    print("{}".format(result))
