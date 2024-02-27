#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 22:20:17 2022

@author: andreluizrodriguesdasilva
"""

import csv

file = open("/home/andreluizrodriguesdasilva/Downloads/color_srgb.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()



with open("/home/andreluizrodriguesdasilva/Downloads/color_srgb.csv") as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]
print(header)
print(rows)


'''
import pandas as pd
print(file.header)
'''
