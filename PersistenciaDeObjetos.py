#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:16:42 2022

@author: andreluizrodriguesdasilva
"""

import pickle
import math

obj1 = math.pi

# Salva no arquivo filename.pickle
with open("filename.pickle", "wb") as f:
    pickle.dump(obj1, f)
    
# Recupera do arquivo filename.pickle
with open("filename.pickle", "rb") as f:
    obj2 = pickle.load(f)