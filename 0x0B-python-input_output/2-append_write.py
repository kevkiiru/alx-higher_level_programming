#!/usr/bin/python3


def append_write(filename="", text=""):
    """Appends text to filename.

    Args:
        filename: name of the file
        text: text to append

    Return: the number of characters added
    """

    with open(filename, 'a+') as f:
        return f.write(text)
