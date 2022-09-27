#!/usr/bin/python3


def read_file(filename=""):
    """Reads from filename and prints it's contents to stdout.

    Args:
        filename: name of the file
    """

    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
