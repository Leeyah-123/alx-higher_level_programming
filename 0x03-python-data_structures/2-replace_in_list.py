#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (idx > 0 and idx < len):
        new_list = my_list
        new_list[idx] = element
        return (new_list)
    return (my_list)
