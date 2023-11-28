#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_d = number % 10
else:
    last_d = ((-number % 10) * -1)

msg = f"Last digit of {number} is {last_d}"

if last_d == 0:
    print(f"{msg} and is 0")
elif last_d > 5 and last_d % 10 != 0:
    print(f"{msg} and is greater than 5")
else:
    print(f"{msg} and is less than 6 and not 0")
