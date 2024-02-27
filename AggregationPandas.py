#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:52:04 2022

@author: andreluizrodriguesdasilva
"""

import seaborn as sns
import numpy as np
import pandas as pd

planets = sns.load_dataset('planets')
planets.shape

planets.head()

# for a Pandas Series the aggregates return a single value
rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
ser

ser.sum()

ser.mean()

# For a DataFrame, by default the aggregates return results within each column:
df = pd.DataFrame({'A': rng.rand(5),
                   'B': rng.rand(5)})
df

df.mean()

# By specifying the axis argument, you can instead aggregate within each row
df.mean(axis='columns')
# df.mean(axis='rows')

# Pandas Series and DataFrames include all of the common aggregates mentioned in
# “Aggregations: Min, Max, and Everything in Between” on page 58; in addition, there
# is a convenience method describe() that computes several common aggregates for
# each column and returns the result. Let’s use this on the Planets data, for now drop‐
# ping rows with missing values:

planets.dropna().describe()


'''GroupBy: Split, Apply, Combine'''
# Split, apply, combine

# While we could certainly do this manually using some combination of the masking,
# aggregation, and merging commands covered earlier, it’s important to realize that the
# intermediate splits do not need to be explicitly instantiated. Rather, the GroupBy can
# (often) do this in a single pass over the data, updating the sum, mean, count, min, or
# other aggregate for each group along the way. The power of the GroupBy is that it
# abstracts away these steps: the user need not think about how the computation is
# done under the hood, but rather thinks about the operation as a whole.

df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data': range(6)}, columns=['key', 'data'])
df

'''We can compute the most basic split-apply-combine operation with the groupby()
method of DataFrames, passing the name of the desired key column:'''
df.groupby('key')
# Out[12]: <pandas.core.groupby.DataFrameGroupBy object at 0x117272160>

# Notice that what is returned is not a set of DataFrames, but a DataFrameGroupBy
# object. This object is where the magic is: you can think of it as a special view of the
# DataFrame, which is poised to dig into the groups but does no actual computation
# until the aggregation is applied. This “lazy evaluation” approach means that common
# aggregates can be implemented very efficiently in a way that is almost transparent to
# the user.

df.groupby('key').sum()
# The sum() method is just one possibility here; you can apply virtually any common
# Pandas or NumPy aggregation function, as well as virtually any valid DataFrame
# operation, as we will see in the following discussion.

planets.groupby('method')['orbital_period'].median()

planets.tail()

# Iteration over groups. The GroupBy object supports direct iteration over the groups,
# returning each group as a Series or DataFrame
for(method, group) in planets.groupby('method'):
    print("{0:30s} shape={1}".format(method, group.shape))

# Dispatch methods. Through some Python class magic, any method not explicitly
# implemented by the GroupBy object will be passed through and called on the groups,
# whether they are DataFrame or Series objects. For example, you can use the
# describe() method of DataFrames to perform a set of aggregations that describe each
# group in the data
planets.groupby('method')['year'].describe().unstack()


'''
Aggregate, filter, transform, apply
The preceding discussion focused on aggregation for the combine operation, but
there are more options available. In particular, GroupBy objects have aggregate(),
filter(), transform(), and apply() methods that efficiently implement a variety of
useful operations before combining the grouped data.'''

rng = np.RandomState(0)
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': rng.randint(0, 10, 6)},
                   columns = ['key', 'data1', 'data2'])


'''Aggregation. We’re now familiar with GroupBy aggregations with sum(), median(),
and the like, but the aggregate() method allows for even more flexibility. It can take
a string, a function, or a list thereof, and compute all the aggregates at once. Here is a
quick example combining all these:'''

df.groupby('key').aggregate(['min', np.median, 'max'])


# Another useful pattern is to pass a dictionary mapping column names to operations
# to be applied on that column
df.groupby('key').aggregate({'data1': 'min',
                            'data2': 'max'})

# Filtering. A filtering operation allows you to drop data based on the group proper‐
# ties. For example, we might want to keep all groups in which the standard deviation is
# larger than some critical value:
def filter_func(x):
    return x['data2'].std()>4

print(df); print(df.groupby('key').std());
print(df.groupby('key').filter(filter_func))

'''The filter() function should return a Boolean value specifying whether the group
passes the filtering. Here because group A does not have a standard deviation greater
than 4, it is dropped from the result.'''

# Transformation. While aggregation must return a reduced version of the data, trans‐
# formation can return some transformed version of the full data to recombine. For
# such a transformation, the output is the same shape as the input. A common example
# is to center the data by subtracting the group-wise mean:
df.groupby('key').transform(lambda x: x - x.mean())


# The apply() method. The apply() method lets you apply an arbitrary function to the
# group results. The function should take a DataFrame, and return either a Pandas
# object (e.g., DataFrame, Series) or a scalar; the combine operation will be tailored to
# the type of output returned.
'''For example, here is an apply() that normalizes the first column by the sum of the
second:'''
def norm_by_data2(x):
    # x is a DataFrame of group values
    x['data1'] /= x['data2'].sum()
    return x

print(df); print(df.groupby('key').apply(norm_by_data2))



'''Specifying the split key
In the simple examples presented before, we split the DataFrame on a single column
name. This is just one of many options by which the groups can be defined, and we’ll
go through some other options for group specification here.'''

# A list, array, series, or index providing the grouping keys. The key can be any series or list
# with a length matching that of the DataFrame. For example:
L = [0, 1, 0, 1, 2, 0]
print(df); print(df.groupby(L).sum())

# Of course, this means there’s another, more verbose way of accomplishing the
# df.groupby('key') from before:
print(df); print(df.groupby(df['key']).sum())

# A dictionary or series mapping index to group. Another method is to provide a dictionary
# that maps index values to the group keys:
df2 = df.set_index('key')
mapping = {'A': 'vowel', 'B': 'consonant', 'C': 'consonant'}
print(df2); print(df2.groupby(mapping).sum())


# Any Python function. Similar to mapping, you can pass any Python function that will
# input the index value and output the group:
print(df2); print(df2.groupby(str.lower).mean())


# A list of valid keys. Further, any of the preceding key choices can be combined to
# group on a multi-index:
df2.groupby([str.lower, mapping]).mean()


'''Grouping example'''
'''As an example of this, in a couple lines of Python code we can put all these together
 and count discovered planets by method and by decade:'''
decade = 10 * (planets['year'] // 10)
decade = decade.astype(str) + 's'
decade.name = 'decade'
planets.groupby(['method', decade])['number'].sum().unstack().fillna(0)
# planets.groupby(['method', decade])['number'].sum().unstack().fillna('#')
# planets.groupby(['method', decade])['number'].sum().unstack()

# This shows the power of combining many of the operations we’ve discussed up to this
# point when looking at realistic datasets. We immediately gain a coarse understanding
# of when and how planets have been discovered over the past several decades!