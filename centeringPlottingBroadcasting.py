#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:51:59 2022

@author: andreluizrodriguesdasilva
"""
import numpy as np

# media com broadcasting
X = np.random.random((10, 3))

# MEAN AGGREGATE ACROSS HE FIRST DIMENSION
Xmean = X.mean(0)
Xmean

# enter the X array by subtracting the mean
X_centered = X - Xmean

X_centered.mean(0)

# Plotting a two-dimensional function
'''
broadcasting is very useful is in displaying images based on two-
dimensional functions. If we want to define a function z = f(x, y), broadcasting can be
used to compute the function across the grid:
'''
# x and y have 50 steps from 0 to 5
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]

z = np.sin(x)**10 + np.cos(x+y*x) *np.cos(x)

#import matplotlib_inline
#%matplotlib inline
import matplotlib.pyplot as plt

plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')
plt.colorbar()