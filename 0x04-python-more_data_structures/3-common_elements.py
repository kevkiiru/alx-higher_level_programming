#!/usr/bin/python3

def common_elements(set_1, set_2):

    setOne = set(set_1)
    setTwo = set(set_2)

    if (setOne & setTwo):
        print(setOne & setTwo)
    else:
        print("No common")
