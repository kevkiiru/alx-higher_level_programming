#!/usr/bin/python3
for a in range(ord('z'), ord('a') -1, -2):
    print("{:c}{:s}".format(c, chr(c - 33)), end="")
