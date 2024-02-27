#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:02:40 2022

@author: andreluizrodriguesdasilva
"""

import pandas as pd
import numpy as np

index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]

populations = [33871648, 37253956,
               18976457, 19378102,
               20851820, 25145561]

pop = pd.Series(populations, index=index)
pop

'''
With this indexing scheme, you can straightforwardly index or slice the series based
on this multiple index
'''
pop[('California', 2010): ('Texas', 2000)]

'''
But the convenience ends there. For example, if you need to select all values from
2010, you’ll need to do some messy (and potentially slow) munging to make it
happen:
'''
pop[[i for i in pop.index if i[1]==2010]]
'''
This produces the desired result, but is not as clean (or as efficient for large datasets)
as the slicing syntax we’ve grown to love in Pandas.
'''

# The better way: Pandas MultiIndex
'''
Fortunately, Pandas provides a better way. Our tuple-based indexing is essentially a
rudimentary multi-index, and the Pandas MultiIndex type gives us the type of opera‐
tions we wish to have. We can create a multi-index from the tuples as follows:
'''
index = pd.MultiIndex.from_tuples(index)
index
# MultiIndex(levels=[['California', 'New York', 'Texas'], [2000, 2010]],
#                      labels=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]])

'''
Notice that the MultiIndex contains multiple levels of indexing—in this case, the state
names and the years, as well as multiple labels for each data point which encode these
levels.
If we reindex our series with this MultiIndex, we see the hierarchical representation
of the data:
'''
pop = pop.reindex(index)
pop
'''
Now to access all data for which the second index is 2010, we can simply use the Pan‐
das slicing notation:
'''
pop[:, 2010]

# MultiIndex as extra dimension
'''
You might notice something else here: we could easily have stored the same data
using a simple DataFrame with index and column labels. In fact, Pandas is built with
this equivalence in mind. The unstack() method will quickly convert a multiply-
indexed Series into a conventionally indexed DataFrame
'''
pop_df = pop.unstack()
pop_df

# Naturally, the stack() method provides the opposite operation
pop_df.stack()
'''
Each extra level in a
multi-index represents an extra dimension of data; taking advantage of this property
gives us much more flexibility in the types of data we can represent. Concretely, we
might want to add another column of demographic data for each state at each year
(say, population under 18); with a MultiIndex this is as easy as adding another col‐
umn to the DataFrame:
'''
pop_df = pd.DataFrame({'total': pop,
                       'under18': [9267089, 9284094,
                                   4687374, 4318033,
                                   5906301, 6879014]})
pop_df


# all the ufuncs and other functionality work with hierarchical indices as well
# Here we compute the
# fraction of people under 18 by year, given the above data:
f_u18 = pop_df['under18'] / pop_df['total']
f_u18.unstack()



# Methods of MultIndex Creation
'''
The most straightforward way to construct a multiply indexed Series or DataFrame
is to simply pass a list of two or more index arrays to the constructor.
'''
df = pd.DataFrame(np.random.rand(4, 2),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=['data1', 'data2'])
df

'''
The work of creating the MultiIndex is done in the background.
Similarly, if you pass a dictionary with appropriate tuples as keys, Pandas will auto‐
matically recognize this and use a MultiIndex by default
'''
data = {('California', 2000): 33871648,
        ('California', 2010): 37253956,
        ('Texas', 2000): 20851820,
        ('Texas', 2010): 25145561,
        ('New York', 2000): 18976457,
        ('New York', 2010): 19378102}
pd.Series(data)
'''
Nevertheless, it is sometimes useful to explicitly create a MultiIndex; we’ll see a cou‐
ple of these methods here.
'''

# Explicit MultiIndex constructors
'''
For more flexibility in how the index is constructed, you can instead use the class
method constructors available in the pd.MultiIndex. For example, as we did before,
you can construct the MultiIndex from a simple list of arrays, giving the index values
within each level:
'''
pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])

''' You can construct it from a list of tuples, giving the multiple index values of each
point'''
pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])

# You can even construct it from a Cartesian product of single indices:
pd.MultiIndex.from_product([['a', 'b'], [1, 2]])

'''
Similarly, you can construct the MultiIndex directly using its internal encoding by
passing levels (a list of lists containing available index values for each level) and
labels (a list of lists that reference these labels):
'''
pd.MultiIndex(levels=[['a', 'b'], [1, 2]],
              labels=[[0, 0, 1, 1], [0, 1, 0, 1]])


# MultiIndex level names

pop.index.names = ['state', 'year']
pop

''' With more involved datasets, this can be a useful way to keep track of the meaning of
various index values'''


# MultiIndex for columns
'''
In a DataFrame, the rows and columns are completely symmetric, and just as the rows
can have multiple levels of indices, the columns can have multiple levels as well. Con‐
sider the following, which is a mock-up of some (somewhat realistic) medical data:
'''



# hierarchical indices and columns
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                     names=['subject', 'type'])
# mock some data (simular alguns dados)
data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10
data += 37

# create the DataFrame
health_data = pd.DataFrame(data, index=index, columns=columns)
health_data
'''
Here we see where the multi-indexing for both rows and columns can come in very
handy. This is fundamentally four-dimensional data, where the dimensions are the
subject, the measurement type, the year, and the visit number. With this in place we
can, for example, index the top-level column by the person’s name and get a full Data
Frame containing just that person’s information:
'''
health_data['Guido']



# Indexing and Slicing a MultiIndex
'''
Indexing and slicing on a MultiIndex is designed to be intuitive, and it helps if you
think about the indices as added dimensions.
'''
# Multiply indexed Series
pop
'''
The MultiIndex also supports partial indexing, or indexing just one of the levels in
the index. The result is another Series, with the lower-level indices maintained:
'''
pop['California']

# Partial slicing is available as well, as long as the MultiIndex is sorted
pop.loc['California': 'New York']

# With sorted indices, we can perform partial indexing on lower levels by passing an
# empty slice in the first index:
pop[:, 2000]

'''
Other types of indexing and selection,
work as well; for example, selection based on Boolean masks:
'''
pop[pop > 22000000]

# Selection based on fancy indexing also works
pop[['California', 'Texas']]


# Multiply indexed DataFrames
'''
A multiply indexed DataFrame behaves in a similar manner. Consider our toy medi‐
cal DataFrame from before
'''
health_data

'''
Remember that columns are primary in a DataFrame, and the syntax used for multi‐
ply indexed Series applies to the columns. For example, we can recover Guido’s heart
rate data with a simple operation:
'''
health_data['Guido', 'HR']

# Also, as with the single-index case, we can use the loc, iloc, and ix indexers
health_data.iloc[:2, :2]

health_data.loc[:, ('Bob', 'HR')]

# página 137

'''Many of
the MultiIndex slicing operations will fail if the index is not sorted.'''
index = pd.MultiIndex.from_product([['a', 'c', 'b'], [1, 2]])
data = pd.Series(np.random.rand(6), index=index)
data.index.names = ['char', 'int']
data

# If we try to take a partial slice of this index, it will result in an error:
try:
    data['a':'b']
except KeyError as e:
    print(type(e))
    print(e)
    
    
'''Pandas provides a number of convenience routines to perform this type of sorting;
examples are the sort_index() and sortlevel() methods of the DataFrame.'''
data = data.sort_index()
data

# With the index sorted in this way, partial slicing will work as expected:
data['a':'b']


''' Stacking and unstacking indices '''
# convert a dataset from a stacked multi-index
# to a simple two-dimensional representation, optionally specifying the level to use
pop.unstack(level=0)

pop.unstack(level=1)

'''The opposite of unstack() is stack(), which here can be used to recover the original
series:'''
pop.unstack().stack()


### Index setting and resetting ###
# turn the index labels into columns
pop_flat = pop.reset_index(name='population')
pop_flat

'''Often when you are working with data in the real world, the raw input data looks like
this and it’s useful to build a MultiIndex from the column values. This can be done
with the set_index method of the DataFrame, which returns a multiply indexed Data
Frame'''
pop_flat.set_index(['state', 'year'])


#### Data Aggregations on Multi-Indices ####
'''built-in data aggregation methods, such as
mean(), sum(), and max() can be passed a
level parameter that controls which subset of the data the aggregate is computed on'''

health_data

# Perhaps we’d like to average out the measurements in the two visits each year. We can
# do this by naming the index level we’d like to explore, in this case the year:
data_mean = health_data.mean(level='year')
data_mean

"""By further making use of the axis keyword, we can take the mean among levels on
the columns as well:"""
data_mean.mean(axis=1, level='type')
'''Thus in two lines, we’ve been able to find the average heart rate and temperature
measured among all subjects in all visits each year. This syntax is actually a shortcut
to the GroupBy functionality, which we will discuss in “Aggregation and Grouping” on
page 158.'''

