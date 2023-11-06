#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return (None)

    list_copy = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > list_copy:
            list_copy = my_list[i]

    return (list_copy)
