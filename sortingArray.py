#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 17:31:43 2022

@author: andreluizrodriguesdasilva
"""

import numpy as np

'''
selection sort repeatedly finds the minimum value from a list,
and makes swaps until the list is sorted. We can code this in just a few lines of Python
'''
def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

x = np.array([2, 1, 4, 3, 5])
selection_sort(x)

# Bogosort
def bogosort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
        return x
    
x = np.array([2, 1, 4, 3, 5])
bogosort(x)

# Fast Sorting in NumPy: np.sort and np.argsort
x = np.array([2, 1, 4, 3, 5])
np.sort(x)

'''
To return a sorted version of the array without modifying the input, you can use
np.sort:
'''

# If you prefer to sort the array in-place, you can instead use the sort method of arrays
x.sort()
print(x)

'''
A related function is argsort, which instead returns the indices of the sorted
elements:
'''
x = np.array([2,1, 4, 3, 5])
i = np.argsort(x)
print(i)

'''
The first element of this result gives the index of the smallest element, the second
value gives the index of the second smallest, and so on. These indices can then be
used (via fancy indexing) to construct the sorted array if desired:
'''
x[i]


# Sorting along rows or columns
rand = np.random.RandomState(42)
X = rand.randint(0, 10, (4, 6))
print(X)

# sort each column of X
np.sort(X, axis=0)

# sort each row of X
np.sort(X, axis=1)

'''
Keep in mind that this treats each row or column as an independent array, and any
relationships between the row or column values will be lost!
'''

# Partial Sorts: Partitioning
'''
Sometimes we’re not interested in sorting the entire array, but simply want to find the
K smallest values in the array. NumPy provides this in the np.partition function.
np.partition takes an array and a number K; the result is a new array with the small‐
est K values to the left of the partition, and the remaining values to the right, in arbi‐
trary order:
'''
x = np.array([7, 2, 3, 1, 6, 5, 4])
np.partition(x, 3)

'''
Similarly to sorting, we can partition along an arbitrary axis of a multidimensional
array:
'''
np.partition(X, 2, axis=1)
# Finally, just as there is a np.argsort that computes indices of the sort, there is a
# np.argpartition that computes indices of the partition.