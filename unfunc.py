#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:26:31 2022

@author: andreluizrodriguesdasilva
"""

# NumPy’s ufuncs

import numpy as np

# Array Arithmetic
x = np.arange(4)
print("x     =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2)

# ufunc for negation, a ** operator for exponentiation, and a %
# operator for modulus
print("-x    = ", -x)
print("x ** 2 = ", x ** 2)
print("x % 2 = ", x % 2)
