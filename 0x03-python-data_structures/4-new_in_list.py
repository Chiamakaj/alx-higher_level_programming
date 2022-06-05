#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp = my_list[:]
    for len in temp:
        len += 0
    if idx < 0 or idx > len:
        return (temp)
    else:
        for i in range(0, len):
            if i == idx:
                temp[i] = element
        return (temp)
