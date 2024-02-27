#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:17:32 2022

@author: andreluizrodriguesdasilva
"""

import numpy as np
import pandas as pd

area = pd.Series({'California': 423967, 'Texas': 695662,
                'New York': 141297, 'Florida': 170312,
                'Illinois': 149995})

pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                'New York': 19651127, 'Florida': 19552860,
                'Illinois': 12882135})

data = pd.DataFrame({'area':area, 'pop':pop})

data['density'] = data['pop'] / data['area']

data.values

# we can transpose the full DataFrame to swap rows and
# columns:
data.T

# passing a single index to an array accesses a row
data.values[0]

# passing a single “index” to a DataFrame accesses a column
data['area']

'''
Using the iloc indexer, we can
index the underlying array as if it is a simple NumPy array (using the implicit
Python-style index), but the DataFrame index and column labels are maintained in
the result:
'''

data.iloc[:3, :2]

data.loc[:'Illinois', :'pop']

# The ix indexer allows a hybrid of these two approaches
data.ix[:3, :'pop']


'''
in the loc indexer we can combine masking and fancy indexing as
in the following
'''

data.loc[data.density > 100, ['pop', 'density']]

'''
Any of these indexing conventions may also be used to set or modify values; this is
done in the standard way that you might be accustomed to from working with
NumPy
'''
data.iloc[0, 2] = 90
data

'''
Additional indexing conventions
There are a couple extra indexing conventions that might seem at odds with the pre‐
ceding discussion, but nevertheless can be very useful in practice. First, while index‐
ing refers to columns, slicing refers to rows:
'''
data['Florida': 'Illinois']
data[1:3]