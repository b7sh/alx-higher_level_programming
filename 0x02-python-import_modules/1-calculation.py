#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
    result1 = sub(a, b)
    print("{} - {} = {}".format(a, b, result1))
    result2 = mul(a, b)
    print("{} * {} = {}".format(a, b, result2))
    result3 = div(a, b)
    print("{} / {} = {}".format(a, b, result3))
