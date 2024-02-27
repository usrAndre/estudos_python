#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 10:28:02 2022

@author: andreluizrodriguesdasilva
"""

# Binning data (CATEGORIZAÇÃO DE DADOS)
import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set() 

np.random.seed(42)
x = np.random.randn(100)

# compute a histogram by hand
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)

# find the appropriate bin for each x
i = np.searchsorted(bins, x)

# add 1 to each of these bins
np.add.at(counts, i, 1)

# plot the results
plt.plot(bins, counts, linestyle='steps');


'''
Of course, it would be silly to have to do this each time you want to plot a histogram.
This is why Matplotlib provides the plt.hist() routine, which does the same in a
single line
'''

plt.hist(x, bins, histtype='step');

# comparando
# digite isso no terminal
print("Numpy routine:")
%timeit counts, edges = np.histogram(x, bins) 
# digite isso no terminal
print("Custom routine:")
%timeit np.add.at(counts, np.searchsorted(bins, x), 1) 


# digite isso no terminal: np.histogram?? para ver como isso é implementado pelo Numpy


# digite isso no terminal
x = np.random.randn(1000000)
print("NumPy routine:")
%timeit counts, edges = np.histogram(x, bins)
# digite isso no terminal
print("Custom routine:")
%timeit np.add.at(counts, np.searchsorted(bins, x), 1)
