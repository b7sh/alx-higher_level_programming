#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = number % -10
elif number > 0:
    last_digit = number % 10
string = f"Last digit of {number} is {last_digit}"
if number > 5:
    print(string, "and is greater than 5")
elif number == 0:
    print(string, "and is 0")
else:
    print(string, "and is less than 6 and not 0")
