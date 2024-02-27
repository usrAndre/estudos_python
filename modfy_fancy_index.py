#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 17:16:00 2022

@author: andreluizrodriguesdasilva
"""
import numpy as np

# Modifying Values with Fancy Index
x = np.arange(10)
i = np.array([2, 1, 8, 4])
x[i] = 99
print(x)

# We can use any assignment-type operator for this. For example
x[i] -= 10
print(x)

x = np.zeros(10)
np.add.at(x, i, 1)
print(x)


