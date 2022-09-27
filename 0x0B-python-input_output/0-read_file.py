#!/usr/bin/python3


def read_file(filename=""):
    """Reads from filename and prints it's contents to stdout
    
    Args:
        filename: name of the file
    """

    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
