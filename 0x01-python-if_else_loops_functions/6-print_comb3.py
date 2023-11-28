#!/usr/bin/python3
number = 0
while number <= 89:
    if number % 10 == 0:
        number += 1 + number // 10
    print("{:02d}".format(number), end=", " if number != 89 else "\n")
    number += 1
