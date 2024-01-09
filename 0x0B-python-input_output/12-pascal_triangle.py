#!/usr/bin/python3
"""a function that returns a list
of lists of integers representing
the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """generate the pascal traingle
    args:
    n (int): the number of rhe row's
    """
    if n <= 0:
        return []

    tringle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = tringle[i - 1][j - 1] + tringle[i - 1][j]
        tringle.append(row)
    return tringle
