#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 13:03:16 2022

@author: andreluizrodriguesdasilva
"""
!head -4 home\andreluizrodriguesdasilva\Área de Trabalho\president_heights.csv
import pandas as pd
import numpy as np


data = pd.read_csv('home\andreluizrodriguesdasilva\Área de Trabalho\president_heights.csv')
heights = np.array(data['heights(cm)'])
print(heights)