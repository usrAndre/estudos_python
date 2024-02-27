#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 15:35:19 2022

@author: andreluizrodriguesdasilva
"""

import numpy as np
import pandas as pd
vals1 = np.array([1, None, 3, 4])
vals1

# None: Pythonic missing data
'''
The first sentinel value used by Pandas is None, a Python singleton object that is often
used for missing data in Python code. Because None is a Python object, it cannot be
used in any arbitrary NumPy/Pandas array, but only in arrays with data type
'object' (i.e., arrays of Python objects)
'''


for dtype in ['object', 'int']:
    print("dtype =" , dtype)
    #%timeit np.arange(1E6, dtype=dtype).sum()
    #print()
    
    
vals1.sum()
# This reflects the fact that addition between an integer and None is undefined    


# NaN: Missing numerical data
'''
The other missing data representation, NaN (acronym for Not a Number), is different;
it is a special floating-point value recognized by all systems that use the standard
IEEE floating-point representation
'''
vals2 = np.array([1, np.nan, 3, 4])
vals2.dtype
'''
Notice that NumPy chose a native floating-point type for this array: this means that
unlike the object array from before, this array supports fast operations pushed into
compiled code. You should be aware that NaN is a bit like a data virus—it infects any
other object it touches. Regardless of the operation, the result of arithmetic with NaN
will be another NaN:
'''
1 + np.nan
0 * np.nan

# NumPy does provide some special aggregations that will ignore these missing values:
vals2.sum(), vals2.min(), vals2.max()

np.nansum(vals2), np.nanmin(vals2), np.nanmax(vals2)
'''
Keep in mind that NaN is specifically a floating-point value; there is no equivalent
NaN value for integers, strings, or other types.
'''


# NaN and None in Pandas
'''
NaN and None both have their place, and Pandas is built to handle the two of them
nearly interchangeably, converting between them where appropriate:
'''
pd.Series([1, np.nan, 2, None])

'''
For types that don’t have an available sentinel value, Pandas automatically type-casts
when NA values are present. For example, if we set a value in an integer array to
np.nan, it will automatically be upcast to a floating-point type to accommodate the
NA
'''
x = pd.Series(range(2), dtype=int)
x

x[0] = None
x
'''
Notice that in addition to casting the integer array to floating point, Pandas automati‐
cally converts the None to a NaN value. (Be aware that there is a proposal to add a
native integer NA to Pandas in the future; as of this writing, it has not been included.)
While this type of magic may feel a bit hackish compared to the more unified
approach to NA values in domain-specific languages like R, the Pandas sentinel/cast‐
ing approach works quite well in practice and in my experience only rarely causes
issues.
'''
'''
Typeclass   Conversion when storing NAs      NA sentinel value
floating     No change                         np.nan
object       No change                         None or np.nan
integer      Cast to float64                   np.nan
boolean      Cast to object                    None or np.nan
'''
# Keep in mind that in Pandas, string data is always stored with an object dtype


# Operating on Null Values
'''
Pandas treats None and NaN as essentially interchangeable for indi‐
cating missing or null values. To facilitate this convention, there are several useful
methods for detecting, removing, and replacing null values in Pandas data structures
'''

'''
isnull()
    Generate a Boolean mask indicating missing values
notnull()
    Opposite of isnull()
dropna()
    Return a filtered version of the data
fillna()
    Return a copy of the data with missing values filled or imputed
'''
# Detecting null values
data = pd.Series([1, np.nan, 'hello', None])
data.isnull()

# Boolean masks can be
# used directly as a Series or DataFrame index
data[data.notnull()]
'''
The isnull() and notnull() methods produce similar Boolean results for Data
Frames
'''

# Dropping nulll values
'''
In addition to the masking used before, there are the convenience methods, dropna()
(which removes NA values) and fillna() (which fills in NA values). For a Series,
the result is straightforward:
'''
data.dropna()

# For a DataFrame, there are more options. Consider the following DataFrame:
df = pd.DataFrame([[1, np.nan, 2],
                   [2, 3, 5],
                   [np.nan, 4, 6]])
df
'''
We cannot drop single values from a DataFrame; we can only drop full rows or full
columns. Depending on the application, you might want one or the other, so
dropna() gives a number of options for a DataFrame.
'''

# By default, dropna() will drop all rows in which any null value is present
df.dropna()
df.dropna(axis=0)


# Alternatively, you can drop NA values along a different axis; axis=1 drops all columns containing a null value:
df.dropna(axis='columns')
df.dropna(axis=1)

'''
But this drops some good data as well; you might rather be interested in dropping
rows or columns with all NA values, or a majority of NA values. This can be specified
through the how or thresh parameters, which allow fine control of the number of
nulls to allow through.
The default is how='any', such that any row or column (depending on the axis key‐
word) containing a null value will be dropped. You can also specify how='all', which
will only drop rows/columns that are all null values:
'''
df[3] = np.nan
df

df.dropna(axis='columns', how='all')
df.dropna(axis='columns', how='any')

'''
For finer-grained control, the thresh parameter lets you specify a minimum number
of non-null values for the row/column to be kept:
'''
df.dropna(axis='rows', thresh=3)
# Here the first and last row have been dropped, because they contain only two non-
# null values.


# Filling null values
'''
Sometimes rather than dropping NA values, you’d rather replace them with a valid
value. This value might be a single number like zero, or it might be some sort of
imputation or interpolation from the good values. You could do this in-place using
the isnull() method as a mask, but because it is such a common operation Pandas
provides the fillna() method, which returns a copy of the array with the null values
replaced
'''
data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
data

# We can fill NA entries with a single value, such as zero:
data.fillna(0)

# We can specify a forward-fill to propagate the previous value forward:
# foward.fill
data.fillna(method='ffill')

# Or we can specify a back-fill to propagate the next values backward:
# back.fill
data.fillna(method='bfill')

'''
For DataFrames, the options are similar, but we can also specify an axis along which
the fills take place:
'''
df
df.fillna(method='ffill', axis=1)
'''
Notice that if a previous value is not available during a forward fill, the NA value
remains.
'''
