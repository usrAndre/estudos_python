#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:56:12 2022

@author: andreluizrodriguesdasilva
"""

import numpy as np

np.random.seed(0) # seed for reproducibility
x1 = np.random.randint(10, size=6) # One-dimensional array
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5)) # Three-dimensional array

# Array Slicing: Accessing Subarrays

''' x[start:stop:step] '''

# Unidimensional Array

x = np.arange(10)
x   # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

x[:5] # first five elements
# array([0, 1, 2, 3, 4])


x[5:] # elements after index 5
# array([5, 6, 7, 8, 9])


x[4:7] # middle subarray
# array([4, 5, 6])


x[::2] # every other element
# array([0, 2, 4, 6, 8])


x[1::2] # every other element, starting at index 1
# array([1, 3, 5, 7, 9])


x[::-1] # all elements, reversed
# array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])


x[5::-2] # reversed every other from index 5
# array([5, 3, 1])


# Multidimensional subarrays
"""
Multidimensional slices work in the same way, 
with multiple slices separated by commas.
For example:
"""   
x2[:2, :3]  # two rows, three columns
x2[:3, ::2] # all rows, every other column

# Finally, subarray dimensions can even be reversed together:
x2[::-1, ::-1]


"""
Accessing array rows and columns. One commonly needed routine is accessing single
rows or columns of an array. You can do this by combining indexing and slicing,
using an empty slice marked by a single colon (:):
"""

print(x2[:, 0])  # first column of x2

print(x2[0, :])  # first row of x2

#In the case of row access, the empty slice can be omitted for a more compact syntax:
print(x2[0])  # equivalent to x2[0, :]


# Subarrays as no-copy views
# extract a 2×2 subarray from this:
print(x2)

x2_sub = x2[:2, :2]
print(x2_sub)

# modify this subarray
x2_sub[0, 0] = 99
print(x2_sub)
# the original array is changed!
print(x2)

# Creating copies of arrays
# method copy()
x2_sub_copy = x2[:2, :2].copy()
print(x2_sub_copy)

# If we now modify this subarray, the original array is not touched:
x2_sub_copy[0, 0] = 42
print(x2_sub_copy)

print(x2)