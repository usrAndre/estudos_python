#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 14:44:09 2022

@author: andreluizrodriguesdasilva
"""
# COMBINING DATASETS
# Concat and Append


import pandas as pd
import numpy as np

'''we’ll define this function, which creates a DataFrame of a particular
form that will be useful below:'''
def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)

# example DataFrame
make_df('ABC', range(3))

# Recall: Concatenation of NumPy Arrays
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
np.concatenate([x, y, z])

'''The first argument is a list or tuple of arrays to concatenate. Additionally, it takes an
axis keyword that allows you to specify the axis along which the result will be
concatenated'''
x = [[1, 2],
     [3, 4]]
np.concatenate([x, x], axis=1)



                ##### PANDAS #####
# Simple Concatenation with pd.concat
''' Pandas has a function, pd.concat(), which has a similar syntax to np.concatenate
but contains a number of options that we’ll discuss momentarily '''


# Signature in Pandas v0.18

# pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
# keys=None, levels=None, names=None, verify_integrity=False,
# copy=True)

ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
pd.concat([ser1, ser2])

# It also works to concatenate higher-dimensional objects, such as DataFrames
df1 = make_df('AB',[1, 2])
df2 = make_df('AB',[3, 4])
print(df1); print(df2);print(pd.concat([df1, df2]))

'''By default, the concatenation takes place row-wise within the DataFrame (i.e.,
axis=0). Like np.concatenate, pd.concat allows specification of an axis along which
concatenation will take place. Consider the following example'''
df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
#print(df3); print(df4); print(pd.concat([df3, df4], axis='col'))
print(df3); print(df4); print(pd.concat([df3, df4], axis=1))


# Duplicate indices
''' One important difference between np.concatenate and pd.concat is that Pandas
concatenation preserves indices, even if the result will have duplicate indices! Consider
this simple example'''
x = make_df('AB', [0, 1])
y = make_df('AB', [2, 3])

y.index = x.index   # make duplicate indices!
print(x); print(y); print(pd.concat([x, y]))

'''Notice the repeated indices in the result. While this is valid within DataFrames, the
outcome is often undesirable. pd.concat() gives us a few ways to handle it'''

# Catching the repeats as an error.
'''you’d like to simply verify that the indices in the
result of pd.concat() do not overlap, you can specify the verify_integrity flag
 With this set to True, the concatenation will raise an exception if there are duplicate
indices'''
try:
    pd.concat([x, y], verify_integrity=True)
except ValueError as e:
    print("ValueError:", e)

'''Ignoring the index. Sometimes the index itself does not matter, and you would prefer
it to simply be ignored. You can specify this option using the ignore_index flag. With
this set to True, the concatenation will create a new integer index for the resulting
Series'''
print(x); print(y); print(pd.concat([x, y], ignore_index=True))


# Adding Multindex keys. 
'''Another alternative is to use the keys option to specify a label
for the data sources; the result will be a hierarchically indexed series containing the
data'''
print(x); print(y); print(pd.concat([x, y], keys=['x', 'y']))

# Concatenation with joins
'''Consider
the concatenation of the following two DataFrames, which have some (but not all!)
columns in common:'''
df5 = make_df('ABC', [1, 2])
df6 = make_df('BCD', [3, 4])
print(df5); print(df6); print(pd.concat([df5, df6]))

'''By default, the entries for which no data is available are filled with NA values. To
change this, we can specify one of several options for the join and join_axes param‐
eters of the concatenate function. By default, the join is a union of the input columns
(join='outer'), but we can change this to an intersection of the columns using
join="inner"'''
print(df5); print(df6);
print(pd.concat([df5, df6], join='inner'))

'''Another option is to directly specify the index of the remaining colums using the
join_axes argument, which takes a list of index objects. Here we’ll specify that the
returned columns should be the same as those of the first input:'''
print(df5); print(df6);
print(pd.concat([df5, df6], join_axes=[df5.columns]))

# The append() method
print(df1); print(df2); print(df1.append(df2))
'''Keep in mind that unlike the append() and extend() methods of Python lists, the
append() method in Pandas does not modify the original object—instead, it creates a
new object with the combined data. It also is not a very efficient method, because it
involves creation of a new index and data buffer. Thus, if you plan to do multiple
append operations, it is generally better to build a list of DataFrames and pass them all
at once to the concat() function'''


# Combining Datasets: Merge and Join
# Categories of Joins:
# ONE-TO-ONE
# MANY-TO-ONE
# MANY-TO-MANY

# One-to-one Joins

#very similar to the column-wise cncatenation
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
'hire_date': [2004, 2008, 2012, 2014]})
print(df1); print(df2)

# To combine this information into a single DataFrame, we can use the pd.merge()
#function:
df3 = pd.merge(df1, df2)
df3


# Many-to-one-Joins

# joins in which one of the two key columns contains duplicate
# entries. For the many-to-one case, the resulting DataFrame will preserve those dupli‐
# cate entries as appropriate. Consider the following example of a many-to-one join:
    
df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
'supervisor': ['Carly', 'Guido', 'Steve']})
print(df3); print(df4); print(pd.merge(df3, df4))


# Many-to-many joins

# Many-to-many joins are a bit confusing conceptually, but are nevertheless well
# defined. If the key column in both the left and right array contains duplicates, then
# the result is a many-to-many merge. This will be perhaps most clear with a concrete
# example. Consider the following, where we have a DataFrame showing one or more
# skills associated with a particular group.
# By performing a many-to-many join, we can recover the skills associated with any
# individual person:
    
df5 = pd.DataFrame({'group': ['Accounting', 'Accounting',
'Engineering', 'Engineering', 'HR', 'HR'],
    'skills': ['math', 'spreadsheets', 'coding', 'linux',
'spreadsheets', 'organization']})
print(df1); print(df5); print(pd.merge(df1, df5))



''' Specification of the Merge Key '''
# We’ve already seen the default behavior of pd.merge(): it looks for one or more
# matching column names between the two inputs, and uses this as the key. However,
# often the column names will not match so nicely, and pd.merge() provides a variety
# of options for handling this.
 
''' The on keyword '''
# Most simply, you can explicitly specify the name of the key column using the on key‐
# word, which takes a column name or a list of column names:
print(df1); print(df2); print(pd.merge(df1, df2, on='employee'))


''' The left_on and right_on keywords '''
# At times you may wish to merge two datasets with different column names; for exam‐
# ple, we may have a dataset in which the employee name is labeled as “name” rather
# than “employee”. In this case, we can use the left_on and right_on keywords to
# specify the two column names:
df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'salary': [70000, 80000, 120000, 90000]})
print(df1); print(df3); print(pd.merge(df1, df3, left_on='employee', right_on='name'))

# The result has a redundant column that we can drop if desired—for example, by
# using the drop() method of DataFrames:

pd.merge(df1, df3, left_on="employee", right_on="name").drop('name', axis=1)
# pd.merge(df1, df3, left_on="employee", right_on="name").drop('salary', axis=1)


'''The left_index and right_index keywords'''
# Sometimes, rather than merging on a column, you would instead like to merge on an
# index. For example, your data might look like this:
df1 = df1.set_index('employee')
df2 = df2.set_index('employee')
print(df1); print(df2)

# You can use the index as the key for merging by specifying the left_index and/or
# right_index flags in pd.merge():
print(df1); print(df2);
print(pd.merge(df1, df2, left_index=True, right_index=True))

# For convenience, DataFrames implement the join() method, which performs a
# merge that defaults to joining on indices:
print(df1); print(df2);
print(df1.join(df2))

# If you’d like to mix indices and columns, you can combine left_index with right_on
# or left_on with right_index to get the desired behavior:
print(df1); print(df3);
print(pd.merge(df1, df3, left_index=True, right_on='name'))



''' Specifying Set Arithmetic for Joins '''

df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'], 
                    'food': ['fish', 'beans', 'bread']},
                   columns = ['name', 'food'])
df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                    'drink': ['wine', 'beer']},
                   columns=['name', 'drink'])
print(df6); print(df7); print(pd.merge(df6, df7))

# Here we have merged two datasets that have only a single “name” entry in common:
# Mary. By default, the result contains the intersection of the two sets of inputs; this is
# what is known as an inner join. We can specify this explicitly using the how keyword,
# which defaults to 'inner':
pd.merge(df6, df7, how='inner')


# Other options for the how keyword are 'outer', 'left', and 'right'. An outer join
# returns a join over the union of the input columns, and fills in all missing values with
# NAs:
print(df6); print(df7); print(pd.merge(df6, df7, how='outer'))

# The left join and right join return join over the left entries and right entries, respec‐
# tively. For example:
print(df6); print(df7); print(pd.merge(df6, df7, how='left'))

# The output rows now correspond to the entries in the left input. Using how='right'
# works in a similar manner.
print(df6); print(df7); print(pd.merge(df6, df7, how='right'))



'''Overlapping Column Names: The suffixes Keyword
Finally, you may end up in a case where your two input DataFrames have conflicting
column names. Consider this example:'''
df8 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'rank': [1, 2, 3, 4]})
df9 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'rank': [3, 1, 4, 2]})
print(df8); print(df9); print(pd.merge(df8, df9, on='name'))
# Because the output would have two conflicting column names, the merge function
# automatically appends a suffix _x or _y to make the output columns unique. If these
# defaults are inappropriate, it is possible to specify a custom suffix using the suffixes
# keyword:
print(df8); print(df9);
print(pd.merge(df8, df9, on='name', suffixes=["_L", "_R"]))
# These suffixes work in any of the possible join patterns, and work also if there are
# multiple overlapping columns.


'''Example: US States Data'''
