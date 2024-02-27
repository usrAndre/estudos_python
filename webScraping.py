#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 12:13:56 2022

@author: andreluizrodriguesdasilva
"""
# web scraping

import requests
from bs4 import BeautifulSoup

params = {
'q':'Python Developer',
'l':'New York State',
}

res = requests.get('https://www.indeed.com/jobs?', params=params)
soup = BeautifulSoup(res.text,'html.parser')

contents=soup.find_all('table','jobCard_mainContent big6_visualChanges')
for item in contents:
    print(item.find('h2','jobTitle').text)
    print(item.find('span', 'companyName').text)
    print(item.find('div','companyLocation').text)