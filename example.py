#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 17:58:29 2022

@author: andreluizrodriguesdasilva
"""

import numpy as np

!head -4 data/president_heights.csv
order,name,height(cm)
1,George  Washington,189
2,John Adams,170
3,ThomasJefferson,189

import pandas as pd
data = pd.read_csv('data/president_heigths.csv')
heights = np.array(data['height(cm)'])
print(heights)