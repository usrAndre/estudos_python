#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:58:42 2022

@author: andreluizrodriguesdasilva
"""

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not found"
        case _:
            return "Something else"
        
# Notice the final block “case _”, the underscore works like a wildcard and will never fail to match. 
# Interestingly, it is possible to combine multiple cases into a single pattern using the pipe operator “|”:

        case 401|403|404:
            return "Not happening"