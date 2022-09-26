# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 23:44:43 2022

@author: Vincent
hw3
prob 3:
"""

# Find the linear regression for CSIRO data on sea level rise around the world.
"""
Created on Mon Sep 19 11:13:26 2022

@author: Vincent
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('CSIRO_Recons_gmsl_mo_2011.txt',float, skiprows=1)

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

print('Humber of data points = ', N)
print('A = {0:5.2f}, +/- {1:5.2f} B = {1:5.2f} '.format(A,B))

chi_square = chi_calc(x,y,sig_y,A,B)
print('chi_square = {0:5.2f}'.format(chi_square))
print('chi_square/dof = {0:6.2f}'.format(chi_square/(N-2)))
print('the correlation coefficient r = {0:5.2f}'.format(r(x,y)))

#plot data points and fits
plt.plot(x,y,'bo')
xc = np.linspace(min(x), max(x),50)
yc = A + B*xc
plt.plot(xc,yc,'r-')

plt.xlim(1880,2020)
plt.ylim(-250,100)
plt.show()

fig, ax = plt.subplots()
res = y - (A + B * x)
ax.plot(x, (A + B*x), 'r-')
ax.scatter(x,y, c= 'b')
ax.vlines(x,y,y-res, 'c')
plt.legend(('Least Squares Fit', 'Data', 'Residuals'),loc = 0)
plt.title('CSIRO Sea Level Data, Church & White (2011)')
plt.xlabel('Year')
plt.ylabel('Sea Level Change (mm)')