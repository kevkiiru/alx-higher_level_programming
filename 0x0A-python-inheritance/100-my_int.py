#!/usr/bin/python3
"""Module MyInt. Inherits from int.
"""


class MyInt(int):
    """Class inheriting from int"""

    def __eq__(self, other):

        return super().__ne__(other)

    def __ne__(self, other):

        return super().__eq__(other)
