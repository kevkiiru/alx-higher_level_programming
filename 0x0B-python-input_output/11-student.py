#!/usr/bin/python3
"""Module student. Main class"""


class Student:
    """class that contains the details of a student"""
    def __init__(self, first_name, last_name, age):
        """details of a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to json"""
        dic = {}
        if attrs is None:
            return self.__dict__
        for a in attrs:
            if hasattr(self, a):
                dic[a] = getattr(self, a)
        return dic

    def reload_from_json(self, json):
        for b, c in json.items():
            if hasattr(self, b):
                setattr(self, b, v)
