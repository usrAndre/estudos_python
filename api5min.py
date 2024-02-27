#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 21:38:46 2022

@author: andreluizrodriguesdasilva
"""

from fastapi import FastAPI
# creating API
app = FastAPI()
# default route
@app.get("/")
async def root():
    return {
        "welcome_message": "Hello hungry Zucky, welcome!",
        "menu": [
            {
            "burgers": "http://localhost:8000/api/v1/menu/burgers"
            },
            {
            "sandwiches": "http://localhost:8000/api/v1/menu/sandwiches"
            }
        ]
    };
# burgers route
@app.get("/api/v1/menu/burgers")
async def burgers():
    return {
    "spicy burger": "10$",
    "cheesy burger": "12$",
    "Extra cheesy spicy burger": "18$"
    }
# sandwiches route
@app.get("/api/v1/menu/sandwiches")
async def sandwiches():
    return {
    "Egg sandwich": "10$",
    "cheesy sandwich": "11$",
    "Chicken sandwich": "13$"
}