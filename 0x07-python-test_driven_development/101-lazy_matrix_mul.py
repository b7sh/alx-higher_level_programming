#!/usr/bin/python3
"""nction that multiplies 2 matrices by using the module NumPy"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """return the multiplication
    args:
    m_a (list of lists): the first matrix
    m_b (list of lists): the second matrix
    """
    return numpy.matmul(m_a, m_b)
