#!/usr/bin/python3
for a in range(ord('z'), ord('a') - 1, -2):
    print("{}{}".format(a, chr(a - 33)), end="")
