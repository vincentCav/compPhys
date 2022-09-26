# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:13:26 2022

@author: Vincent
"""

#leastsqrs.py
#construct a least squares fit and determine goodness of the fit
#plot the data and fitted curve

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

#plot data points and fit
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

####################MONTE CARLO FOLLOWS
N_trial = 1000 
FitParms = np.array([])
A_values = np.zeros(N_trial)
B_values = np.zeros(N_trial)
unc_A_values = np.zeros(N_trial)
unc_B_values = np.zeros(N_trial)

y_err = np.sqrt(sum((y - (A + B*x))**2)/(N-2))
xmin = x[0]
xmax = x[-1]

#create random data
for j in range(N_trial):
    #CREATE AS MANY X VALUES AS IN THE ORIGINAL RANGE OF DATA
    xTrial = np.random.uniform(xmin, xmax, size=N)
    yTrial = A + B*xTrial + np.random.normal(loc=0,scale=y_err,size=N)
    A_values[j], B_values[j], unc_A_values[j], unc_B_values[j] = leastsqrs(xTrial, yTrial)

plt.hist(A_values, bins = 50)
plt.show()

A = np.mean(A_values)
B = np.mean(B_values)
unc_A = np.mean(unc_A_values)
unc_B = np.mean(unc_B_values)

print('The best straight line fit is y = {0:4.2e} +/- {1:4.2e} + ({2:4.2e} +/- {3:5.2e})*x'.format(A, B,unc_A,unc_B))

#multiaxis histogram
fig = plt.figure(figsize = (6,6))
fig.suptitle = ('Monte Carlo Estimation of Parameters')
grid = plt.GridSpec(4,4,hspace=0.4,wspace=0.5)
main_ax = fig.add_subplot(grid[:-1,1:])
y_hist = fig.add_subplot(grid[-1,0], xticklabels = [], sharey = main_ax )
x_hist = fig.add_subplot(grid[-1,1], yticklabels = [], sharex = main_ax )

#scatter poitns on the main axes
main_ax.plot(A_values, B_values, 'ok', markersize = 2, alpha = 0.2)

#histogram on the attached axes
x_hist.hist(A_values, 50, histtype='stepfilled', orientation='vertical', color='blue')
x_hist.invert_yaxis()
y_hist.hist(B_values, 50, histtype='stepfilled', orientation='horizontal', color='green')
y_hist.invert_xaxis()
plt.show()

