#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 12:47:30 2022

@author: andreluizrodriguesdasilva
"""

import numpy as np

x = np.array([1, 2, 3])

# row vector via reshape
x.reshape((1, 3))

# row vector via newaxis
x[np.newaxis, :]

#column vector via reshape
x.reshape((3, 1))

# column vector via newaxis
x[:, np.newaxis]



x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])

# vertically stack the arrays
np.vstack([x, grid])

# horizontally stack the arrays
y = np.array([[99],
              [99]])
np.hstack([grid, y])

# Splitting of Arrays
x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)
# Notice that N split points lead to N + 1 subarrays

''' related functions np.hsplit
and np.vsplit'''

grid = np.arange(16).reshape((4, 4))
grid

upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower)

left, right = np.hsplit(grid, [2])
print(left)
print(right)