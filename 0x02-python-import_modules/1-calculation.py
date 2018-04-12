#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    w = add(a, b)
    print("{} + {} = {}".format(a, b, w))
    x = sub(a, b)
    print("{} - {} = {}".format(a, b, x))
    y = mul(a, b)
    print("{} * {} = {}".format(a, b, y))
    z = div(a, b)
    print("{} / {} = {}".format(a, b, z))
