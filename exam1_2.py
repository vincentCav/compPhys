# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 00:24:47 2022

@author: Vincent
exam 1 problem 2
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("WASP24TESSexcerpt.csv",dtype=float,delimiter =",")

x, y = data[:,0],data[:,1]

plt.plot(x,y,'b.')

sortedData = np.sort(data,1)

np.savetxt("sorted_WASP24TESSexcerpt.csv",sortedData,delimiter=",",fmt="%s")