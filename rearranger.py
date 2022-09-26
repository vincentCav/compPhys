# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 13:30:39 2022

@author: Vincent
hw2_2
"""

import numpy as np

data = np.genfromtxt("TOI311133118excerpt.txt",delimiter=",",dtype=float)

data = data[np.argsort(data[:,1])]

np.savetxt('rearrange.txt',data,delimiter=' ',fmt='%s')