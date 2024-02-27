#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:04:04 2022

@author: andreluizrodriguesdasilva
"""
import numpy as np
from math import e
import math

'''
a = 2
c = 3

a, c = c, a
'''
# Número de Euler
print(e)

math.exp(1)

# raiz quadrada
math.sqrt(48)
math.sqrt(81)

a = np.array([[1, 2], [3, 4]])
print(a.shape)

print(a.T) # matriz Transposta de a

b = np.array([[3, 4], [5, 6]])

print(a * b) # Produto simples

print(a + b) # Soma

# Multiplicação de Matrizes (linha X coluna)
a1 = np.array([[1, 2]])
a1.shape == (1,2) # matriz a1 tem 1 linha e 2 colunas
b1 = np.array([[3, 4],[5, 6]])
b1.shape == (2,2)   # matriz b1 tem 2 linhas e 2 colunas
# Multiply
mm = np.dot(a1,b1)
mm == [13, 16]
mm.shape == (1,2)