#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 20:14:08 2022

@author: andreluizrodriguesdasilva
"""
# Conjuntos
# set
a = {1, 2, 3, 3, 2, 4, 5, 5}
b = {4, 6, 7, 9, 3}
# Performs the Intersection of 2 sets and prints them
print(a & b)
# Performs the Union of 2 sets and prints them
print(a | b)
# Performs the Difference of 2 sets and prints them
print(a - b)
# Performs the Symmetric Difference of 2 sets and prints them
print(a ^ b)


# lista
list = ["One", "Two", "Three"]
# join function
s = ','.join(list)
print(s)

# split function
newList = s.split(',')
print(newList)
