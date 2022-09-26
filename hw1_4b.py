# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 13:30:39 2022

@author: Vincent
hw2_4b
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("sunspots.txt",dtype=float)

data1000 = data[0:1000]

month, sunspots = data1000[:,0], data1000[:,1]

plt.plot(month,sunspots,"o")

print(data1000)