#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 16:32:52 2022

@author: andreluizrodriguesdasilva
"""
import numpy as np

x = np.array([1, 2, 3, 4, 5])
x < 3   # less than
x > 3   # greater than
x <= 3  # less than or equal
x >= 3  # greater than or equal
x != 3  # not equal
x == 3  # equal

'''
It is also possible to do an element-by-element comparison of two arrays, and to
include compound expressions:
'''
(2 * x) == (x ** 2)

rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))
x

x< 6

print(x)

# count the number of True entries in a Boolean array, np.count_nonzero is useful:
# how many values less than 6?
np.count_nonzero(x < 6)

# outro jeito de obter a mesma informação
# use np.sum; in this case, False is interpreted as 0, and True is inter‐
# preted as 1:
np.sum(x <  6)

'''
The benefit of sum() is that like with other NumPy aggregation functions, this sum‐
mation can be done along rows or columns as well:
'''
# how many values less than 6 in each row?
np.sum(x < 6, axis=1)