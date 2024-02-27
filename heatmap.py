#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:02:15 2022

@author: andreluizrodriguesdasilva
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

Z = np.random.uniform(0, 1, (8,8))

ax.imshow(Z)