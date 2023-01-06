#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    length = len(sys.argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = sys.argv[2]
    if operator != "+" and operator != "-" and operator != "*" and operator != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    result = 0
    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    else:
        result = div(a, b)

    print("{} {} {} = {}".format(a, operator, b, result))
