# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:17:07 2022

@author: Vincent
hw1_1.py
"""

import numpy as np

data = np.genfromtxt("tess2022112184951-s0051-0000000460396820-0223-s_lc_t1.txt",delimiter=",",dtype= str,missing_values="NULL")


clean_data = np.empty(3, dtype=str)
for i in data:
    for j in i:
        clean = True
        if j == '"NULL"':
            clean = False
    if clean == True:
        clean_data = np.vstack([clean_data, i])

np.savetxt("clean_data.txt",clean_data,delimiter=" ",fmt='%s')