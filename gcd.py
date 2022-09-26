# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:35:39 2022

@author: Vincent
"""

"""
Documentation
"""
def gcd(m,n):
    if n == 0:
        return m
    else:
        return gcd(n,m % n)
m = int(input("What is the first number to consider?"))
n = int(input("What is the second number to consider?"))
print(gcd(108,180))