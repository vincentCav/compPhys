# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 22:23:52 2022

@author: Vincent
hw_3
prob 4
"""

import numpy as np
import matplotlib.pyplot as plt

#Date	  Time	Julian Date	  Value	  StD
#dtype = np.dtype([("Date", str), ("Time", str), ("Julian Date", int), ("Value", float), ("StD", float)])
data = np.loadtxt("Global_O2_Concentration_2010_2020.txt",float,skiprows=1)

print(data)

date = np.array(data[0])
value = np.array(data[3])
sigma = np.array(data[4])

print(date)