# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 16:29:10 2022

@author: Vincent
Prints the catalan numbers <= 10 billion.
Catalan #s are:
    C_0 = 1
    C_n+1 = (4n + 2)*C_n/(n + 2)
"""

def getCatalanNumbers():
    arr = []
    i = 1
    n = 1
    while i <= 10000000000:
        arr.append(i)
        i = int((4*n + 2) * i / (n + 2))
        n += 1
    return arr

print(getCatalanNumbers())
