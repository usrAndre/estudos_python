#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 11:11:02 2022

@author: andreluizrodriguesdasilva
"""

def soma_mult(a, b):
    soma = a+b
    mult = a*b
    
    return soma, mult


soma_mult(2, 3)
print('soma 2 e 3: ',soma_mult(2,3)[0])
print('multiplica 2 e 3: ',soma_mult(2,3)[1])
