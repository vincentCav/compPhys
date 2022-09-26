# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 16:35:04 2022

@author: Vincent
"""

def collatzOf20(n):
    for i in range(20):
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1
        print(n)
        
        
collatzOf20(230)