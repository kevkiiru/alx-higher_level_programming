#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if num >= 1:
        print("arguments: ".format(num))
    for a in range(1, num):
        print("{}: {}".format(a, sys.argv[a]))