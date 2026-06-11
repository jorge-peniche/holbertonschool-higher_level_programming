#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(str(number)[-1]) * -1 if number < 0 else int(str(number)[-1])
stament = ''
if last == 0 :
    stament = 'and is 0'
elif last > 5:
    stament = 'and is greater than 5'
elif last < 6:
    stament = 'the string and is less than 6 and not 0'
print(f"Last digit of {number} is {last} {stament}")
