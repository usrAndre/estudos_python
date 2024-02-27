#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:32:04 2022

@author: andreluizrodriguesdasilva
"""

import numpy as np
x = np.array([-2, -1, 0, 1, 2])
abs(x)

np.absolute(x)

np.abs(x)

# This ufunc can also handle complex data, 
# in which the absolute value returns the magnitude

x = np.array([3-4j, 4-3j, 2+0j, 0+1j])
np.abs(x)


# Trigonometric functions

# defining an array of angles
theta = np.linspace(0, np.pi, 3)

print("theta      = ", theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))

# Inverse trigonometric functions
x = [-1, 0, 1]

print("x         = ", x)
print("arcsin(x) = ", np.arcsin(x))
print("arccos(x) = ", np.arccos(x))
print("arctan(x) = ", np.arctan(x))

# Exponents and logarithms
x = [1, 2, 3]

print("x    =", x)
print("e^x  =", np.exp(x))
print("2^x  =", np.exp2(x))
print("3^x  =", np.power(3, x))


# base-2 logarithm or the base-10 logarithm
x = [1, 2, 4, 10]

print("x        =", x)
print("ln(x)    =", np.log(x))
print("log2(x)  =", np.log2(x))
print("log10(x) =", np.log10(x))

# specialized versions that are useful 
# for maintaining precision with very small input
x = [0, 0.001, 0.01, 0.1]

print("exp(x) - 1 =", np.expm1(x))
print("log(1 + x) =", np.log1p(x))
