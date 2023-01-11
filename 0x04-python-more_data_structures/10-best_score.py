#!/usr/bin/python3
def best_score(a_dictionary):
    keys = list(a_dictionary)

    if len(keys) == 0:
        return (None)

    highest_score = a_dictionary[0]
    for i in keys:
        if a_dictionary[i] > highest_score:
            highest_score = a_dictionary[i]

    return (highest_score)
