#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:24:43 2023

@author: andrluizrodriguesdasilva
"""

def plus(*args):
    total = 0
    for i in args:
        total += i
    
    return total

print(plus(20,30,40,50))


print(plus(23.18, -77.53))