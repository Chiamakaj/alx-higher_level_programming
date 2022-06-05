#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for len in my_list:
        len += 0
    if idx < 0 or idx > len:
        return (my_list)
    else:
        for i in range(0, len):
            if i == idx:
                my_list[i] = element
        return (my_list)
