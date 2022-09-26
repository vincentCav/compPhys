# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:46:16 2022

@author: Vincent
exam1_5.py
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('antarctica_mass_200204_202006.txt',float, skiprows=31)

x = np.array(data[:,0]) # independent variable - (year.decimal)
y = np.array(data[:,1]) # dependent variable - Antarctic mass (Gigatonnes)
sig_y = np.array(data[:,2]) # standard deviation - Antarctic mass uncertainty (Gigatonnes)
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

#Find the Pearson correlation coefficient for the data.
print('a) the correlation coefficient r = {0:5.2f}'.format(r(x,y)))

#Determine the linear regression for the data.
A, B, sig_A, sig_B = leastsqrs(x, y)
print('b) The linear regression is Y = AX + B')
print('   where A = {0:5.2f}, B = {1:5.2f} '.format(A,B))


print("c) starting now")
#Plot the data and the model curve (linear regression).
plt.plot(x,y,'bo')
xc = np.linspace(min(x), max(x),50)
yc = A + B*xc
plt.plot(xc,yc,'r-')
plt.legend(('Least Squares Fit', 'Data', 'Residuals'),loc = 0)
plt.title('Antarctic mass measurements, GRACE, 04/2002 - 06/2020')
plt.xlabel('TIME (year)')
plt.ylabel('Antarctic mass (gigatonnes)')
plt.show()
print("   ...finished.")

#Evaluate the goodness of the fit.
print("d) The fit of the linear regression closely matches the data. It's good.")

#What do you note about yearly and decadal changes in mass?
print("e) It has a downward slope of about 143 gigatonnes per year.")

