# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 13:30:39 2022

@author: Vincent
hw2_4a
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("sunspots.txt",dtype=float)

month, sunspots = data[:,0], data[:,1]

plt.plot(month,sunspots,"o")

print(data)