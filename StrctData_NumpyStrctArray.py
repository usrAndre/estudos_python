#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 10:35:15 2022

@author: andreluizrodriguesdasilva
"""
import numpy as np

name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

x = np.zeros(4, dtype=int)

# Use a compound data type for structured arrays
data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                      'formats':('U10', 'i4', 'f8')})
print(data.dtype)

'''
Here 'U10' translates to “Unicode string of maximum length 10,” 'i4' translates to
“4-byte (i.e., 32 bit) integer,” and 'f8' translates to “8-byte (i.e., 64 bit) float.”
'''
# Now that we’ve created an empty container array, 
# we can fill the array with our lists of values:
data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)

# Get all names
data['name']

# Get first row of data
data[0]

# Get the name from the last row
data[-1]['name']

'''
Using Boolean masking, this even allows you to do some more sophisticated opera‐
tions such as filtering on age:
'''
# Get the names where age is under 30
data[data['age'] < 30]['name']

# Creating Structured Arrays

'''Structured array data types can be specified in a number of ways. Earlier, we saw the
dictionary method:'''

np.dtype({'names':('name', 'age', 'weight'),
'formats':('U10', 'i4', 'f8')})
# Out[10]: dtype([('name', '<U10'), ('age', '<i4'), ('weight', '<f8')])
'''For clarity, numerical types can be specified with Python types or NumPy dtypes
instead:'''
np.dtype({'names':('name', 'age', 'weight'),
'formats':((np.str_, 10), int, np.float32)})
# Out[11]: dtype([('name', '<U10'), ('age', '<i8'), ('weight', '<f4')])

# A compound type can also be specified as a list of tuples:
np.dtype([('name', 'S10'), ('age', 'i4'), ('weight', 'f8')])
# Out[12]: dtype([('name', 'S10'), ('age', '<i4'), ('weight', '<f8')])
'''If the names of the types do not matter to you, you can specify the types alone in a
comma-separated string:'''
np.dtype('S10,i4,f8')
# Out[13]: dtype([('f0', 'S10'), ('f1', '<i4'), ('f2', '<f8')])
'''
# Table 2-4. NumPy data types
Character Description                    Example
'b'         Byte                         np.dtype('b')
'i'         Signed integer               np.dtype('i4') == np.int32
'u'         Unsigned integer             np.dtype('u1') == np.uint8
'f'         Floating point               np.dtype('f8') == np.int64
'c'         Complex floating point       np.dtype('c16') == np.complex128
'S', 'a'    string                       np.dtype('S5')
'U'         Unicode string               np.dtype('U') == np.str_
'V'         Raw data (void)              np.dtype('V') == np.void
'''

# More Advanced Compoud Types
tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3, 3))])
X = np.zeros(1, dtype=tp)
print(X[0])
print(X['mat'][0])
'''
If we view our data as a record array instead, we can access this with slightly fewer
keystrokes:
'''
data_rec = data.view(np.recarray)
data_rec.age

# no terminal:
'''
%timeit data['age']
%timeit data_rec['age']
%timeit data_rec.age
'''