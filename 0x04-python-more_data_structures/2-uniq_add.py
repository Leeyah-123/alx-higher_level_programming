#!/usr/bin/python3
def uniq_add(my_list=[]):
    sorted_list = []
    for i in range(len(my_list)):
        if my_list[i] not in sorted_list:
            sorted_list.append(my_list[i])

    result = 0
    for i in range(len(sorted_list)):
        result += sorted_list[i]

    return (result)
