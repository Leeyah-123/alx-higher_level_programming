#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)

    top = 0
    bottom = 0

    for i in my_list:
        score = my_list[0]
        weight = my_list[1]

        top += score * weight
        bottom += weight

    return (top / bottom)
