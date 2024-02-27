#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:52:30 2023

@author: andrluizrodriguesdasilva
"""

def func1(a, b):
    return a / b

def func2(x):
    a = x
    b = x - 1
    
    return func1(a, b)

func2(3)