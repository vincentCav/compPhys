# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 13:30:39 2022

@author: Vincent
hw2_4c.py
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("sunspots.txt",dtype=float)

data1000 = data[0:1000]

month, sunspots = data1000[:,0], data1000[:,1]

r = 5
sunspotsAvg = [(sum(sunspots[(i - r):(i + r)]) / (2 * r + 1)) for i in range(1000)]
print(sunspotsAvg)

plt.plot(month,sunspots,"y")
plt.plot(month,sunspotsAvg,"y",color="red")

print(data1000)