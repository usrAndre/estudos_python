#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 15:28:54 2022

@author: andreluizrodriguesdasilva
"""

# Creating a DataFrameby passing a numpy array, with a datetime index and labeled columns:

import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
dates

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))           


a = 5
b = 7
print(a + b)

print(a/b)

print(a//b)


