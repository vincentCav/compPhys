# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 13:30:39 2022

@author: Vincent
hw2_3
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("TOI311133118excerpt.txt",delimiter=",",dtype=float)

Flux, Time = data[:,0], data[:,1]

data = data[np.argsort(data[:,1])]

x = data[:,0]
y = data[:,1]
err = data[:,2]

plt.errorbar(x,y,err, marker = 'o', color = 'b', capsize = 2, ls = 'none')
plt.plot(Flux,Time, 'y')

plt.xlabel("Flux (W/m^2)")
plt.ylabel("Time (days)")

np.savetxt('rearrange.txt',data,delimiter=' ',fmt='%s')