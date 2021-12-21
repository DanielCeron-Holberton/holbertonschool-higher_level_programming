#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
lastDigit_string = "Last digit of {} is {} and"
less_string = "is less than 6 and not 0"
greater_string = "and is greater than 5"

if number >= 0:
    last_digit = number % 10
else:
    last_digit = number % -10

if last_digit < 6 and last_digit != 0:
    print(lastDigit_string.format(number, last_digit), less_string)
elif last_digit > 5:
    print(lastDigit_string.format(number, last_digit), greater_string)
else:
    print(lastDigit_string.format(number, last_digit), "and is 0")
