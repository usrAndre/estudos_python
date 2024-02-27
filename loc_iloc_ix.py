#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 16:40:42 2022

@author: andreluizrodriguesdasilva
"""

import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])
data

data['b']

'a' in data

data.keys()

list(data.items())

# Series objects can even be modified with a dictionary-like
data['e'] = 1.25
data

# Series as one-dimensional array
'''
Series builds on this dictionary-like interface and provides array-style item selec‐
tion via the same basic mechanisms as NumPy arrays—that is, slices, masking, and
fancy indexing
'''
# slicing by explicit index
data['a':'c']

# slicing by implicit integer index
data[0:2]

# masking
data[(data > 0.3) & (data < 0.8)]

# fancy indexing
data[['a', 'e']]

'''
Among these, slicing may be the source of the most confusion. Notice that when you
are slicing with an explicit index (i.e., data['a':'c']), the final index is included in
the slice, while when you’re slicing with an implicit index (i.e., data[0:2]), the final
index is excluded from the slice.
'''

# Indexers: loc, iloc, and ix
data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
data

# explicit index when indexing
data[1]

# implicit index when slicing
data[1:3]

'''
Pandas provides
some special indexer attributes that explicitly expose certain indexing schemes.
'''
# loc attribute allows indexing and slicing that always references the explicit
# index
data.loc[1]
data.loc[1:3]

# iloc attribute allows indexing and slicing that always references the implicit
# Python-style index
data.iloc[1]
data.iloc[1:3]
'''
indexing attribute, ix, is a hybrid of the two, and for Series objects is equiva‐
lent to standard []-based indexing
'''

# One guiding principle of Python code is that “explicit is better than implicit.”


# Data Selection in DataFrame
# DataFrame as a dictionary

area = pd.Series({'California': 423967, 'Texas': 695662,
'New York': 141297, 'Florida': 170312,
'Illinois': 149995})

pop = pd.Series({'California': 38332521, 'Texas': 26448193,
'New York': 19651127, 'Florida': 19552860,
'Illinois': 12882135})

data = pd.DataFrame({'area': area, 'pop':pop})
data

data['area']
# Equivalently, we can use attribute-style access with column names that are strings
data.area

data.area is data['area']
'''
Embora esta seja uma abreviação útil, tenha em mente que não funciona para todos os casos!
Por exemplo, se os nomes das colunas não forem strings ou se os nomes das colunas entrarem em conflito
com métodos do DataFrame, esse acesso estilo atributo não é possível.
'''
data.pop is data['pop']
# saída: false

'''
Em particular, você deve evitar a tentação de tentar a atribuição de colunas via atributo
(ou seja, use data['pop'] = z em vez de data.pop = z)
'''
# with the Series objects discussed earlier, this dictionary-style syntax can also be
# used to modify the object, in this case to add a new column:
data['density'] = data['pop'] / data['area']
data