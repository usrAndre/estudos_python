#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 10:33:07 2022

@author: andreluizrodriguesdasilva
"""

import numpy as np

# Specifying output
x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
print(y)

'''
    This can even be used with array views. For example, we can write the results of a
computation to every other element of a specified array:
'''
y = np.zeros(10)
np.power(2, x, out=y[::2])
print(y)


# Aggregates
# interesting aggregates that can be computed
# directly from the object
x = np.arange(1, 6)

np.add.reduce(x)

np.multiply.reduce(x)

np.add.accumulate(x)

np.multiply.accumulate(x)



# Outer products
# ufunc can compute the output of all pairs of two different inputs using
# the outer method

x = np.arange(1,6)
np.multiply.outer(x, x)
