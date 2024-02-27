#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:11:04 2022

@author: andreluizrodriguesdasilva
"""

import numpy as np
# Fancy Indexing
rand = np.random.RandomState(42)

x = rand.randint(100, size=10)
print(x)

[x[3], x[7], x[2]]

# passing an array of indices to access
# multiple array elements at once

ind = [3, 7, 4]
x[ind]

'''
    With fancy indexing, the shape of the result reflects the shape of the index arrays
    rather than the shape of the array being indexed:
'''
ind = np.array([[3, 7],
                [4, 5]])
x[ind]

# Fancy indexing also works in multiple dimensions
X = np.arange(12).reshape((3, 4))
X

'''
Like with standard indexing, the first index refers to the row, and the second to the
column:
'''
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
X[row, col]

# Broadcasting: if we combine a column vector and a row vector within the indices, we
# get a two-dimensional result
X[row[:, np.newaxis], col]

row[:, np.newaxis] * col

'''
fancy indexing can be combined with the other
indexing schemes we’ve seen:
'''
print(X)
X[2, [2, 0, 1]]

X[1:, [2, 0, 1]]

# And we can combine fancy indexing with masking:
mask = np.array([1, 0, 1, 0], dtype=bool)
X[row[:, np.newaxis], mask]
