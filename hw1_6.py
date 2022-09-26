# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:11:06 2022

@author: Vincent
hw2_6.py
"""

import numpy as np
import matplotlib.pyplot as plt
import math


def r(x):
    factor_1 = math.e ** math.sin(x)
    factor_2 = 2 * math.cos(4*x)
    factor_3 = math.sin(x / 12) ** 5
    
    return factor_1 - factor_2 + factor_3

def toTheta(i):
    return i * math.pi / 10
    
to24 = range(24 * 10)

theta = list(map(toTheta, to24))
radius = list(map(r,theta))

plt.polar(theta,radius)