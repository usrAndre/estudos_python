#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 12:14:14 2022

@author: andreluizrodriguesdasilva
"""
# OPERANTING ON DATA IN PANDAS

import pandas as pd
import numpy as np


# Ufuncs: Index Preservation
rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0, 10, 4))
ser

df = pd.DataFrame(rng.randint(0, 10, (3, 4)),
                  columns=['A', 'B', 'C', 'D'])
df

'''
If we apply a NumPy ufunc on either of these objects, the result will be another Pan‐
das object with the indices preserved
'''
np.exp(ser)
# Or, for a slightly more complex calculation
np.sinc(df * np.pi / 4)


# UFuncs: Index Alignment
'''
For binary operations on two Series or DataFrame objects, Pandas will align indices
in the process of performing the operation. This is very convenient when you are
working with incomplete data, as we’ll see in some of the examples that follow.
'''
# Index alignment in Series
area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
                  'California': 423967}, name='area')
population = pd.Series({'California': 38332521, 'Texas': 26448193, 
                       'New York': 19651127}, name='population')
population / area

# The resulting array contains the union of indices of the two input arrays, which we
# could determine using standard Python set arithmetic on these indices

area.index | population.index

A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
A + B

'''
If using NaN values is not the desired behavior, we can modify the fill value using
appropriate object methods in place of the operators. For example, calling A.add(B)
is equivalent to calling A + B, but allows optional explicit specification of the fill value
for any elements in A or B that might be missing:
'''
A.add(B, fill_value=0)

# Index alignment in DataFrame
'''
A similar type of alignment takes place for both columns and indices when you are
performing operations on DataFrames
'''
A = pd.DataFrame(rng.randint(0, 20,(2, 2)),
                 columns=list('AB'))
A

B = pd.DataFrame(rng.randint(0, 10,(3, 3)),
                 columns=list('BAC'))
B

A + B
'''
Notice that indices are aligned correctly irrespective of their order in the two objects,
and indices in the result are sorted. As was the case with Series, we can use the asso‐
ciated object’s arithmetic method and pass any desired fill_value to be used in place
of missing entries. Here we’ll fill with the mean of all values in A (which we compute
by first stacking the rows of A):
'''
fill = A.stack().mean()
A.add(B, fill_value=fill)