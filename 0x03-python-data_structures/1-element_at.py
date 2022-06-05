#!/usr/bin/python3
def element_at(my_list, idx):
    for len in my_list:
        len += 0
    if idx < 0 or idx > len:
        return(None)
    else:
        for i in range(0, len):
            if i == idx:
                return(my_list[i])
