#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 17:13:07 2022

@author: andreluizrodriguesdasilva
"""

import speedtest

def internet_speed():
    # Checking download speed
    d_speed = speedtest.Speedtest()
    # Checking upload speed
    up_speed = speedtest.Speedtest()
    print(f'Download speed is {d_speed.download()/8000000:.2f}mb',
          f'and upload speed is {up_speed.upload()/8000000:.2f}mb')
    
internet_speed()
    