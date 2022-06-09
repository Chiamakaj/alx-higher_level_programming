#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        col = 0
        elm = 0
        for tupl in my_list:
            col += (tupl[0] * tupl[1])
            elm += tupl[1]
        return (col / elm)
    return 0
