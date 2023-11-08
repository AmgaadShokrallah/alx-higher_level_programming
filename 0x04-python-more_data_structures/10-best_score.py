#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    maxv = list(a_dictionary.keys())[0]
    maxk = a_dictionary[maxv]
    for k, v in a_dictionary.items():
        if v > maxk:
            maxk = v
            maxv = k
    return (maxv)
