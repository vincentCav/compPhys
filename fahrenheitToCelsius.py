# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:11:16 2022

@author: Vincent
tempconvert.py
Converts Fahrenheit to Celsius
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
    

X =[]
for i in range(32,213,10):
    X.append(i)

Y = [(x-32)*5/9 for x in X]
print(Y)
fig, ax = plt.subplots()
ax.plot(X, Y, color="green",marker="D")
fig.savefig("figure.pdf")
fig.show()
