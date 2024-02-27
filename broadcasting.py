#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:25:06 2022

@author: andreluizrodriguesdasilva
"""

import numpy as np

'''
    NumPy’s broadcasting functionality. Broadcasting is simply a
set of rules for applying binary ufuncs (addition, subtraction, multiplication, etc.) on
arrays of different sizes.
'''

a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
a + b

a + 5

M = np.ones((3, 3))
M

M + a

a = np.arange(3)
b = np.arange(3)[:, np.newaxis]

print(a)
print(b)

a + b


