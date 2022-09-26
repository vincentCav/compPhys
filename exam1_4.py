# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 00:59:08 2022

@author: Vincent\
exam1_4
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def sumFunction(n):
    val = np.float64(math.factorial(4*n) * (1103 + 26390*n) /((math.factorial(n) ** 4) * 396**(4*n)))
    return val

def convergeToPi(n):
    sum = 0
    sum = 1 / (np.float64(np.sum([sumFunction(i) for i in range(n)]) * 2 * math.sqrt(2) / 9801))
    return sum

print(convergeToPi(1))
print(convergeToPi(2))
print(np.pi)