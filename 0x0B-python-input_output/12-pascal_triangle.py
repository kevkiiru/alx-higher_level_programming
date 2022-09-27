#!/usr/bin/python3
"""Module pascal_triangle.
"""


def pascal_triangle(n):
    """function that returns a list of lists of integers representing the
    Pascal's triangle of n
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for a in range(1, n):
        row = [1]
        for b in range(1, x):
            row.append(triangle[x-1][y-1] + triangle[x-1][y-1])
        row.append(1)
        triangle.append(row)
    return triangle
