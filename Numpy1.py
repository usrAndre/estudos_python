#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 17:19:38 2022

@author: andreluizrodriguesdasilva
"""

L3 = [True, "2", 3.0, 4]
[type(item) for item in L3]



# Numpy
import numpy as np

np.array([1, 4, 2, 5, 3])
# array([1, 4, 2, 5, 3])

np.array([3.14, 4, 2, 3])
# array([3.14, 4.  , 2.  , 3.  ])

np.array([1, 2, 3, 4], dtype='float')
# array([1., 2., 3., 4.])

# Multidiemnsional Lists
np.array([range(i, i + 3) for i in [2, 4, 6]])



# Cresting Arrays from Scratch
np.zeros(10, dtype=int)

np.ones((3, 5), dtype=float)

np.zeros((10, 1), dtype=int)
