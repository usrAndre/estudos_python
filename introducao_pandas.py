#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 15:31:09 2022

@author: andreluizrodriguesdasilva
"""
# verifica a versão do pandas/ numpy (bibliotecas)
import pandas as pd
pd.__version__

import numpy
numpy.__version__

import numpy as np

# pd? para ver a documentação no terminal ou pd.<TAB> p/ namespace

'''Pandas Series'''
data = pd.Series([0.25, 0.5, 0.75, 1.0])
data

data.values
data.index

data[1]
data[1:3]

# explicit index definition gives the Series object additional capabilities
'''For example, if we wish, we can use strings as an index:'''
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
data

data['b']

'''
make the Series-as-dictionary analogy even more clear by constructing a
Series object directly from a Python dictionary
'''
population_dict = {'California': 38332521,
              'Texas': 26448193,
              'New York': 19651127,
              'Florida': 19552860,
              'Illinois': 12882135}
population = pd.Series(population_dict)
population

# Unlike a dictionary, though, the Series also supports array-style operations such as
# slicing
population['California']

population['California':'Illinois']

population['Texas':'Florida']

# data can be a scalar, which is repeated to fill the specified index:
pd.Series(5, index=[100, 200, 300])

# data can be a dictionary, in which index defaults to the sorted dictionary keys:
pd.Series({2:'a', 1:'b', 3:'c' })

# In each case, the index can be explicitly set if a different result is preferred
pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2])

# The Pandas DataFrame Object
# DataFrame as a generalized NumPy array
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297, 'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
area
'''
Now that we have this along with the population Series from before, we can use a
dictionary to construct a single two-dimensional object containing this information:
'''
states = pd.DataFrame({'population': population,
                       'area': area})
states

states.index

states.columns



# DataFrame as specialized dictionary
states['area']

'''
Constructing DataFrame objects
A Pandas DataFrame can be constructed in a variety of ways. Here we’ll give several
examples.
'''
# From a single Series object. A DataFrame is a collection of Series objects, and a single-
# column DataFrame can be constructed from a single Series:
pd.DataFrame(population, columns=['population'])

'''
From a list of dicts. Any list of dictionaries can be made into a DataFrame. We’ll use a
simple list comprehension to create some data:
'''
data = [{'a': i, 'b': 2 * i}
        for i in range(3)]
pd.DataFrame(data)

# Even if some keys in the dictionary are missing, Pandas will fill them in with NaN (i.e.,
# “not a number”) values
pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])

'''
From a dictionary of Series objects. As we saw before, a DataFrame can be constructed
from a dictionary of Series objects as well:
'''
pd.DataFrame({'population': population,
              'area': area})

'''
From a two-dimensional NumPy array. Given a two-dimensional array of data, we can
create a DataFrame with any specified column and index names. If omitted, an integer
index will be used for each:
'''
pd.DataFrame(np.random.rand(3, 2),
             columns=['foo', 'bar'],
             index=['a', 'b', 'c'])

'''
From a NumPy structured array. A Pandas DataFrame operates much like a
structured array, and can be created directly from one:
'''
A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
A

pd.DataFrame(A)

# The Pandas Index Object
'''
This Index object is an interesting
structure in itself, and it can be thought of either as an immutable array or as an
ordered set (technically a multiset, as Index objects may contain repeated values)
'''
ind = pd.Index([2, 3, 5, 7, 11])
ind

'''
Index as immutable array
The Index object in many ways operates like an array. For example, we can use stan‐
dard Python indexing notation to retrieve values or slices
'''
ind[1]
ind[::2]
# Index objects also have many of the attributes familiar from NumPy arrays:
print(ind.size, ind.shape, ind.ndim, ind.dtype)

'''
One difference between Index objects and NumPy arrays is that indices are immuta‐
ble—that is, they cannot be modified via the normal means:
'''
ind[1] = 0

# Index as ordered set
'''
Pandas objects are designed to facilitate operations such as joins across datasets,
which depend on many aspects of set arithmetic. The Index object follows many of
the conventions used by Python’s built-in set data structure, so that unions, intersec‐
tions, differences, and other combinations can be computed in a familiar way:
'''
indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])

indA & indB  # intersection
indA | indB  # union
indA ^ indB  # symetric difference
