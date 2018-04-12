#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if (sys.argv[2] == "+"):
        print("{} + {} = {}".format(a, b, a+b))
    elif (sys.argv[2] == "-"):
        print("{} - {} = {}".format(a, b, a-b))
    elif (sys.argv[2] == "*"):
        print("{} * {} = {}".format(a, b, a*b))
    elif (sys.argv[2] == "/"):
        print("{} / {} = {}".format(a, b, a/b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
