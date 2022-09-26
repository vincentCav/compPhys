# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 23:26:12 2022

@author: Vincent
hw 3
prob 2:
"""

import math
import numpy as np
import matplotlib.pyplot as plt

xc = np.linspace(0, 40, 20)
yc = [10,12,15,8,13,14,19,18,11,13,7,8,11,8,12,6,13,8,6]
print(len(yc))

plt.hist(yc,bins=5)

print("The mean is {0:5.2f}".format(np.mean(yc)))
print("The standard deviation is {0:5.2f}".format(np.std(yc)))

print("No, I don't get roughly equal values. What's going on?")
