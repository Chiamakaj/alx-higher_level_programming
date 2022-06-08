#!/usr/bin/python3
def uniq_add(my_list=[]):
    sel = set(my_list)
    sum = 0
    for i in sel:
        sum += i
    return sum
