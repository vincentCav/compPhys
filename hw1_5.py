# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 16:24:47 2022

@author: Vincent
hw2_5.py
"""

import numpy as np
import matplotlib.pyplot as plt

v0 = 20.0
g = 9.81

time = range(0,60)
y = [(v0 * (x / 10) - g * (x / 10) ** 2 / 2) for x in time]

plt.plot(time,y,"y")

print("The max is ", max(y), "at time", x[max])