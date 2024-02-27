#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 17:24:03 2022

@author: andreluizrodriguesdasilva
"""
import numpy as np

rand = np.random.RandomState(42)
mean = [0, 0]
cov = [[1, 2],
       [2, 5]]

X = rand.multivariate_normal(mean, cov, 100)
X.shape

# %matiplotlib inline
#import matplotlib_inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set() # for plot styling


'''
Let’s use fancy indexing to select 20 random points. We’ll do this by first choosing 20
random indices with no repeats, and use these indices to select a portion of the origi‐
nal array
'''
plt.scatter(X[:, 0], X[:, 1]);

indices = np.random.choice(X.shape[0], 20, replace=False)
indices

selection = X[indices] # fancy indexing here
selection.shape

plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
plt.scatter(selection[:, 0], selection[:, 1],facecolor='none', s=200);