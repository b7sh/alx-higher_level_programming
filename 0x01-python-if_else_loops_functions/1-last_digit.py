#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = number % -10
elif number > 0:
    last_digit = number % 10
string = f"last digit of {number} is {last_digit}"
if last_digit > 5:
    print(string, "and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(string, "and is less than 6 and not zero")
else:
    print(string, "and is zero")