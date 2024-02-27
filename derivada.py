#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:44:01 2022

@author: andreluizrodriguesdasilva
"""

from sympy import *
import numpy as np

# derivada da função x^2 + 1 com a função diff() da biblioteca SymPy
# Especificamos o símbolo como x com a função Symbol() 
# e calculamos a derivada em relação ao símbolo x

x = Symbol('x')
y = x**2 + 1

yprime = y.diff(x)
print(yprime)


# Integrais
import sympy as sp
x = sp.symbols('x')
f=x**2
sp.integrate(f,x)

mu, sigma, alfa, teta = 3, 1, 0, 8