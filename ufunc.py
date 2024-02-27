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

-(0.5*x + 1) ** 2

np.add(x, 2)
np.negative(2)
np.multiply(2, 3)
np.divide(3, 2)
np.floor_divide(3, 2)
np.power(3, 2)
np.mod(9, 4)
'''
    Operator Equivalent ufuncDescription
    +Addition (e.g., 1 + 1 = 2)
    np.add
    -np.subtractSubtraction (e.g., 3 - 2 = 1)
    -np.negativeUnary negation (e.g., -2)
    *np.multiplyMultiplication (e.g., 2 * 3 = 6)
    /np.divideDivision (e.g., 3 / 2 = 1.5)
    //np.floor_divide Floor division (e.g., 3 // 2 = 1)
    **np.powerExponentiation (e.g., 2 ** 3 = 8)
    %np.modModulus/remainder (e.g., 9 % 4 = 1)
'''