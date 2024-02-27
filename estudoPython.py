#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:22:07 2022

@author: andreluizrodriguesdasilva
"""

example = ['Sunday', 'Monday', 'Tuesday', 'Wednesday']
print(example[-1])
print(example[-2])
print(example[-4])
print(example[-4] == example[0])

# slicing: process of accessing a part or subset of a given list
print(example[0:2])
print(example[-3:-1])


# Função que pega erro de lista
def lista(i, list):
    try:
        list[i]
    except IndexError as e:
        print(e)
    finally:
        print(list[i])
        
lista(8, example)
lista(2, example)
    

###########################################
def lista(i, list):
    try:
        list[i]
    except ValueError as e:  # ValueError
        print(e)
    finally:
        print(list[i])