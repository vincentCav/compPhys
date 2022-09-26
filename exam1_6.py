# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:39:09 2022

@author: Vincent
"""

import numpy as np
import matplotlib.pyplot as plt

def analyze(file):
    data = np.loadtxt(file,float, skiprows=1)
    
    x = np.array(data[:,0]) # independent variable
    y = np.array(data[:,1]) # dependent variable
    sig_y = np.array(data[:,2]) # standard deviation
    N = len(x)              #number of data points
    
    #define least squares fit
    def leastsqrs(x,y):
        #initialize our variables
        sum_x = 0
        sum_y = 0
        sum_xy = 0
        sum_xx = 0
        A = 0
        B = 0
        
        #perform sums
        sum_x = np.sum(x)
        sum_y = np.sum(y)
        sum_xx = np.inner(x, x)
        sum_xy = np.inner(x, y)
        
        # determine the coefficients A and B
        Delta = N*sum_xx  - sum_x*sum_x
        A = (sum_xx*sum_y - sum_x*sum_xy) / Delta
        B = (N*sum_xy - sum_x*sum_y) / Delta
        sig_A = np.mean(sig_y)*np.sqrt(np.sum(x**2 / Delta))
        sig_B = np.mean(sig_y)*np.sqrt(N / Delta)
        
        return [A,B,sig_A, sig_B]
    
    # Calculate chi square
    def chi_calc(x,y,sig_y,A,B):
        chi_square = 0
        chi_square = np.sum(((y - (A + B * x)) ** 2) / (2 * sig_y ** 2))
        return chi_square
    
    #Define the correlation coefficient
    def r(x,y):
        r = 0
        sum_diff_xy = 0
        sum_xdiff_squared = 0
        sum_ydiff_squared = 0
        x_bar = np.mean(x)
        y_bar = np.mean(y)
        sum_xdiff_squared = np.sum((x - x_bar)**2)
        sum_ydiff_squared = np.sum((y - y_bar)**2)
        sum_diff_xy = np.sum((x - x_bar)*(y - y_bar))
        r = sum_diff_xy/np.sqrt(sum_xdiff_squared*sum_ydiff_squared)
        return r
    
    A, B, sig_A, sig_B = leastsqrs(x, y)
    
    print("For {0}".format(file))
    print('  Number of data points = ', N)
    print('  A = {0:5.2f}, +/- {1:5.2f} (Mpc), B = {2:5.2f} +/- {3:5.2f} (km/s)'.format(A,sig_A,B,sig_B))
    print('  The slope of the straight line, {0:5.2f} (km/s), is the Hubble- Lemaître constant.'.format(B))
    
    
    chi_square = chi_calc(x,y,sig_y,A,B)
    print('  chi_square = {0:5.2f}'.format(chi_square))
    print('  chi_square/dof = {0:6.2f}'.format(chi_square/(N-2)))
    print('  the correlation coefficient r = {0:5.2f}'.format(r(x,y)))
    print("  I don't think we need the uncertainty of r")
    print("\n====================================================\n")

def analyzeModd(file):
    data = np.loadtxt(file,float, skiprows=1)
    
    x = np.array(data[:,0]) # independent variable
    y = np.array(data[:,1]) # dependent variable
    sig_y = np.array(data[:,2]) # standard deviation
    N = len(x)              #number of data points
    
    #define least squares fit
    def leastsqrs(x,y):
        #initialize our variables
        sum_x = 0
        sum_y = 0
        sum_xy = 0
        sum_xx = 0
        A = 0
        B = 0
        
        #perform sums
        sum_x = np.sum(x)
        sum_y = np.sum(y)
        sum_xx = np.inner(x, x)
        sum_xy = np.inner(x, y)
        
        # determine the coefficients A and B
        Delta = N*sum_xx  - sum_x*sum_x
        A = (sum_xx*sum_y - sum_x*sum_xy) / Delta
        B = (N*sum_xy - sum_x*sum_y) / Delta
        sig_A = np.mean(sig_y)*np.sqrt(np.sum(x**2 / Delta))
        sig_B = np.mean(sig_y)*np.sqrt(N / Delta)
        
        return [A,B,sig_A, sig_B]
    
    # Calculate chi square
    def chi_calc(x,y,sig_y,A,B):
        chi_square = 0
        chi_square = np.sum(((y - (A + B * x)) ** 2) / (2 * sig_y ** 2))
        return chi_square
    
    #Define the correlation coefficient
    def r(x,y):
        r = 0
        sum_diff_xy = 0
        sum_xdiff_squared = 0
        sum_ydiff_squared = 0
        x_bar = np.mean(x)
        y_bar = np.mean(y)
        sum_xdiff_squared = np.sum((x - x_bar)**2)
        sum_ydiff_squared = np.sum((y - y_bar)**2)
        sum_diff_xy = np.sum((x - x_bar)*(y - y_bar))
        r = sum_diff_xy/np.sqrt(sum_xdiff_squared*sum_ydiff_squared)
        return r
    
    A, B, sig_A, sig_B = leastsqrs(x, y)
    
    B = np.sum(x*y) / np.sum(x*x)
    
    print("MODDED: For {0}".format(file))
    print('  Number of data points = ', N)
    print('  A = {0:5.2f}, +/- {1:5.2f} (Mpc), B = {2:5.2f} +/- {3:5.2f} (km/s)'.format(A,sig_A,B,sig_B))
    print('  The slope of the straight line, {0:5.2f} (km/s), is the Hubble- Lemaître constant.'.format(B))
    
    
    chi_square = chi_calc(x,y,sig_y,A,B)
    print('  chi_square = {0:5.2f}'.format(chi_square))
    print('  chi_square/dof = {0:6.2f}'.format(chi_square/(N-2)))
    print('  the correlation coefficient r = {0:5.2f}'.format(r(x,y)))
    print("  I don't think we need the uncertainty of r")
    print("\n====================================================\n")

analyze("Lemaitre.txt")
analyze("Hubble.txt")
analyzeModd("Lemaitre.txt")
analyzeModd("Hubble.txt")

print("From your analysis, which data set has the stronger correlation?")
print("   The Hubble data has a better correlation,since B = 439.51 in Hubble's and that changes\n only slightly to 412.91 with a better estimate.\n")
print("Which data set has the better chi-squared per degrees of freedom?")
print("   The better chi-squared would be the smaller chi-squared, which is B at 22.24.\n")
print("For which data set does the value of the Hubble-Lemaître constant remain nearly the same for non-zero and zero intercept?")
print("   The value remains the same for Hubble's the most, from 439.51 to 412.91.")
print("Whose data would you say was better?  Why?")
print("   Hubble's data was better. It minimized the coefficients for Hubble, and its constant remained more constant :)")



