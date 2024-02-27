#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 16:39:45 2022

@author: andreluizrodriguesdasilva
"""

import numpy as np

L = np.random.random(100)
sum(L)

np.sum(L) # muito mais rápido

big_array = np.random.rand(1000000)


min(big_array), max(big_array)

np.min(big_array), np.max(big_array) # muito mais rápido

# shorter syntax NumPy aggregates
print(big_array.min(), big_array.max(), big_array.sum())

# multidimensional aggregation
M = np.random.random((3, 4))
print(M)

M.sum()

# find the minimum value within each
# column by specifying axis=0
M.min(axis=0)

# find the maximum value within each
# row by specifying axis=0
M.min(axis=1)
'''
np.sum        np.nansum        Compute sum of elements
np.prod       np.nanprod       Compute product of elements
np.mean       np.nanmean       Compute median of elements
np.std        np.nanstd        Compute standard deviation
np.var        np.nanvar        Compute variance
np.min        np.nanmin        Find minimum value
np.max        np.nanmax        Find maximum value
np.argmin     np.nanargmin     Find index of minimum value
np.argmax     np.nanargmax     Find index of maximum value
np.median     np.nanmedian     Compute median of elements
np.percentile np.nanpercentile Compute rank-based statistics of elements
np.any        N/A              Evaluate whether any elements are true
np.all        N/A              Evaluate whether all elements are true
'''