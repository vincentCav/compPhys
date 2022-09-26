# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 22:04:24 2022

@author: Vincent
hw 3
prob 1 : chi-square-probability-function
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def calculate_probability(chi_square,v):
    val = 0
    denominator = (2**(v / 2)) * math.gamma(v / 2)
    numerator = (math.e ** (chi_square / 2)) * (chi_square) ** ((v / 2) - 1)
    val = numerator / denominator
    return val

print(math.gamma(3))

v = 4
xc = np.linspace(0,28,100)
yc_4 = [calculate_probability(chi_square, v) for chi_square in xc]

v = 10
yc_10 = [calculate_probability(chi_square, v) for chi_square in xc]

plt.plot(xc,yc_4,'r-')
plt.plot(xc,yc_10,'b-')
plt.title("1. Chi-square probability function")
plt.xlabel('Chi-square')
plt.ylabel("Probability")

print('The maximum where v = 4 is {0:5.2f}'.format(max(yc_4)))
print('The maximum where v = 10 is {0:5.2f}'.format(max(yc_10)))
print("I don't think probabilities work like that?")