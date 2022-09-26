# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 14:25:47 2022

@author: Vincent
"""

import math


def sinEstimation(n,x):
    """
    

    Parameters
    ----------
    n : TYPE
        The amount of repetitions in the sum function.
    x : int
        The x which would be used in sin(x).

    Returns
    -------
    sum : TYPE
        DESCRIPTION.

    """
    sum = 0
    for j in range(n):
        z = (-1)**j
        y = x**(2*j + 1)
        fac = math.factorial((2*j) + 1)
        sum+=z*y/fac
    return sum

def sinDifference(n,x):
    return abs(sinEstimation(n,x) - math.sin(x))

def sinError(n,x):
    return sinDifference(n, x) / math.sin(x)

print(sinError(250,20))