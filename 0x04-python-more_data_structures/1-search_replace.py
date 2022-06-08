#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def swap_y(obj):
        return (obj if obj != search else replace)
    return (list(map(swap_y, my_list)))
