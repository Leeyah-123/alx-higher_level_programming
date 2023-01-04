#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b > 0:
        for i in range(0, b):
            result = a * result
    else:
        result = a
        for i in range(1, b * -1):
            result = a / result
    return result
