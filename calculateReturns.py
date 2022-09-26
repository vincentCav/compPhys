# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 14:00:40 2022

Calculates interest
@author: Vincent
"""
import math


def calculateReturns(P,t,PMT,r,n):
    """
    

    Parameters
    ----------
    P : Int
        Initial deposit.
    t : Int
        Time in months that the money is invested.
    PMT : Int
        Additional monthly contribution.
    r : Float
        Annual interest rate.
    n : Float
        Number of times that interest is compounded per unit t.

    Returns
    -------
    Float
        Total return on investment after time t.

    """
    initial = P*math.pow((1+r/n), n*t)
    monthlyContribution = PMT*(math.pow(1+r/n,n*t) - 1)/(r/n)
    print("The return on investment for the rate ", r, "is", "$"+str(int(initial + monthlyContribution)))

P=100
PMT=100
t=480
n=0.25
for r in [0.020,0.018,0.028,0.03]:
    calculateReturns(P, t, PMT, r, n)