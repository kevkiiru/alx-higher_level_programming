#!/usr/bin/python3
def max_integer(my_list=[]):
    new_list = len(my_list)
    if new_list == 0:
        return 'None'
    else:
        new_list.sort()
