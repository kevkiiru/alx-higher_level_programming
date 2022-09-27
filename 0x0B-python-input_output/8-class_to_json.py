#!/usr/bin/python3
"""Module class_to_json. Main function
"""


import json


def class_to_json(obj):
    """returns the dictionary desctiption with simple data structure(list,
    dictionary, string, integer and boolean) for JSON serialization of an
    object.
    """
    return obj.__dict__
