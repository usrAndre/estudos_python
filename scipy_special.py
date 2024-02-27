#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:48:57 2022

@author: andreluizrodriguesdasilva
"""

import numpy as np
from scipy import special


# Gama functions (generalized factorials) and related functions
x = [1, 5, 10]
print("gamma(x)      =", special.gamma(x))
print("ln|gamma(x)|  =", special.gammaln(x))
print("beta(x, 2)    =", special.beta(x, 2))

# Error function (integral of Gaussian)
# its complement, and its inverse
x = np.array([0, 0.3, 0.7, 1.0])
print("erf(x) =", special.erf(x))
print("erfc(x) =", special.erfc(x))
print("erfinv(x) =", special.erfinv(x))


L = np.random.random(100)
sum(L)