#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 20:51:12 2022

@author: andreluizrodriguesdasilva
"""

from fastapi import FastAPI

# creating API
app = FastAPI()

# default route
@app.get("/")
async def root():
    return{
        "welcome_message": "Hello hungry Zucky, welcome!",
        "menu": [
            {
                "burgers": "https://localhost:8000/api/v1/menu/burgers"
            },
            {
                "sandwiches": "https://localhost:8000/api/v1/menu/sandwiches"
            }
        ]
    };

# burgers route
@app.get("/api/v1/menu/burgers")
async def burgers():
    return{
        "spyce burger": "10$",
        "cheese burger": "12$",
        "Extra cheese spyce burger": "18$"
    }

# sandwiches route
@app.get("/api/v1/menu/sandwiches")
async def sandwiches():
    return{
        "egg sandwich": "10$",
        "chesse sandwich": "11$",
        "Chicken sandwich": "13$"
    }