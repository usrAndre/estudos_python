#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:32:23 2022

@author: andreluizrodriguesdasilva
"""
# Metaclass
# Everything is an object and have a class
# default class is type


class Foo(object):
    pass

bar = Foo()

print(type(bar))
print(type(Foo))
print(type(type))