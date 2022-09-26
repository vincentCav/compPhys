# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 00:41:02 2022

@author: Vincent
Exam1_3
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def madelung(x):
    # It seems that i, j, k, are always equal. Therefore, I simply use x for all three.
    if x == 0:
        return 0
    val = 1 / math.sqrt((x**2) * 3)
    if x % 2 == 1:
        val = val * -1
    return val

L = 100

iteration = range(L*-1, L+1)

madelung_sum = np.sum([madelung(i) for i in iteration])

print("The Madelung constant is {0:10f} for when L = {1}".format(madelung_sum,L))