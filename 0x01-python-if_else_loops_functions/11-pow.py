#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b > 0:
        for i in range(0, b):
            result = a * result
    else:
        for i in range(0, b):
            result = a / result
    return result
