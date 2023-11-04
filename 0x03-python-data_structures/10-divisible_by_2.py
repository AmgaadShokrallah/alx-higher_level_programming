#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    listmult = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            listmult.append(True)
        else:
            listmult.append(False)

    return (listmult)
