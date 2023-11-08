#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    maxk = list(a_dictionary.keys())[0]
    maxv = a_dictionary[maxk]
    for k, v in a_dictionary.items():
        if v > maxv:
            maxv = v
            maxk = k
    return (maxk)
