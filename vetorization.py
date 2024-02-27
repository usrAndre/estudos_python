#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 17:11:56 2022

@author: andreluizrodriguesdasilva
"""

'''Vectorized String Operations'''

# One strength of Python is its relative ease in handling and manipulating string data.
# Pandas builds on this and provides a comprehensive set of vectorized string operations
# that become an essential piece of the type of munging required when one is working
# with (read: cleaning up) real-world data. In this section, we’ll walk through some of
# the Pandas string operations, and then take a look at using them to partially clean up
# a very messy dataset of recipes collected from the Internet.

''' Introducing Pandas Operations '''
# We saw in previous sections how tools like NumPy and Pandas generalize arithmetic
# operations so that we can easily and quickly perform the same operation on many
# array elements. For example:
    

import numpy as np
x = np.array([2, 3, 5, 7, 11, 13])
x * 2

# This vectorization of operations simplifies the syntax of operating on arrays of data:
# we no longer have to worry about the size or shape of the array, but just about what
# operation we want done. For arrays of strings, NumPy does not provide such simple
# access, and thus you’re stuck using a more verbose loop syntax:

data = ['peter', 'Paul', 'MARY', 'gUIDO']
[s.capitalize() for s in data]

# This is perhaps sufficient to work with some data, but it will break if there are any
# missing values. For example:
    
data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
[s.capitalize() for s in data]

# Pandas includes features to address both this need for vectorized string operations
# and for correctly handling missing data via the str attribute of Pandas Series and
# Index objects containing strings. So, for example, suppose we create a Pandas Series
# with this data:
    
import pandas as pd
names = pd.Series(data)
names

# We can now call a single method that will capitalize all the entries, while skipping
# over any missing values:

names.str.capitalize()

# Using tab completion on this str attribute will list all the vectorized string methods
# available to Pandas.

'''Tables of Pandas String Methods'''
# If you have a good understanding of string manipulation in Python, most of Pandas’
# string syntax is intuitive enough that it’s probably sufficient to just list a table of avail‐
# able methods; we will start with that here, before diving deeper into a few of the sub‐
# tleties. The examples in this section use the following series of names:
    
monte = pd.Series(['Graham Chapman', 'John Cleese', 'Terry Gilliam',
                   'Eric Idle', 'Terry Jones', 'Michael Palin'])

### Methods Similar to Python String Methods ###
'''
len()        lower()       translate()    ljust()
upper()      startswith()
isupper()    islower()     
rjust()      find()    endswith()    isnumeric()
center()     rfind()   isalnum()     isdecimal()
zfill()      index()   isalpha()     split()
strip()      rindex()  isdigit()     rsplit()
rstrip()     capitalize()            isspace()
partition()  lstrip()                swapcase()
rpartition() istitle()
'''
monte.str.lower()
monte.str.len()
monte.str.startswith('T')
monte.str.split()

# Methods using regular expressions
# In addition, there are several methods that accept regular expressions to examine the
# content of each string element, and follow some of the API conventions of Python’s
# built-in re module

'''
MethodDescription
match()             Call re.match() on each element, returning a Boolean.
extract()           Call re.match() on each element, returning matched groups as strings.
findall()           Call re.findall() on each element.
replace()           Replace occurrences of pattern with some other string.
contains()          Call re.search() on each element, returning a Boolean.
count()             Count occurrences of pattern.
split()             Equivalent to str.split(), but accepts regexps.
rsplit()            Equivalent to str.rsplit(), but accepts regexps.
'''

# With these, you can do a wide range of interesting operations. For example, we can
# extract the first name from each by asking for a contiguous group of characters at the
# beginning of each element:
    
monte.str.extract('([A-Za-z]+)')

# Or we can do something more complicated, like finding all names that start and end
# with a consonant, making use of the start-of-string (^) and end-of-string ($) regular
# expression characters:

monte.str.findall(r'^[^AEIOU].*[^aeiou]$')

# Miscellaneous methods
# Finally, there are some miscellaneous methods that enable other convenient opera‐
# tions
'''
Method              Description
get()               Index each element
slice()             Slice each element
slice_replace()     Replace slice in each element with passed value
cat()               Concatenate strings
repeat()            Repeat values
normalize()         Return Unicode form of string
pad()               Add whitespace to left, right, or both sides of strings
wrap()              Split long strings into lines with length less than a given width
join()              Join strings in each element of the Series with passed separator
get_dummies()       Extract dummy variables as a DataFrame
'''

# monte.get(2)
# monte.pad()

# Vectorized item access and slicing. The get() and slice() operations, in particular,
# enable vectorized element access from each array. For example, we can get a slice of
# the first three characters of each array using str.slice(0, 3). Note that this behav‐
# ior is also available through Python’s normal indexing syntax—for example,
# df.str.slice(0, 3) is equivalent to df.str[0:3]:
    
monte.str[0:3]

# Indexing via df.str.get(i) and df.str[i] is similar.
# These get() and slice() methods also let you access elements of arrays returned by
# split(). For example, to extract the last name of each entry, we can combine
# split() and get():
    
monte.str.split().str.get(-1)

'''
Indicator variables. Another method that requires a bit of extra explanation is the
get_dummies() method. This is useful when your data has a column containing some
sort of coded indicator. For example, we might have a dataset that contains informa‐
tion in the form of codes, such as A=“born in America,” B=“born in the United King‐
dom,” C=“likes cheese,” D=“likes spam”:
'''
full_monte = pd.DataFrame({'name': monte,
                           'info': ['B|C|D', 'B|D', 'A|C', 'B|D', 'B|C',
                                    'B|C|D']})
full_monte

# The get_dummies() routine lets you quickly split out these indicator variables into a
# DataFrame:

full_monte['info'].str.get_dummies('|')

# With these operations as building blocks, you can construct an endless range of string
# processing procedures when cleaning your data.

''' Exemple: Recipe Database '''