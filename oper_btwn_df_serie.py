#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 17:06:00 2022

@author: andreluizrodriguesdasilva
"""
# Ufuncs: Operations Between DataFrame and Series

import numpy as np
import pandas as pd

rng = np.random.RandomState(42)

A = rng.randint(10, size=(3, 4))
A

A - A[0]
'''
subtraction between a two-dimensional array and one of its rows is
applied row-wise.
'''
# In Pandas, the convention similarly operates row-wise by default
df = pd.DataFrame(A, columns=list('QRST'))
df - df.iloc[0]

'''
If you would instead like to operate column-wise, you can use the object methods
mentioned earlier, while specifying the axis keyword
'''
df.subtract(df['R'], axis=0)

'''
Note that these DataFrame/Series operations, like the operations discussed before,
will automatically align indices between the two elements:
'''
halfrow = df.iloc[0, ::2]
halfrow

df - halfrow

'''
This preservation and alignment of indices and columns means that operations on
data in Pandas will always maintain the data context, which prevents the types of silly
errors that might come up when you are working with heterogeneous and/or mis‐
aligned data in raw NumPy arrays.
'''