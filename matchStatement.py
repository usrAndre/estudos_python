#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:46:12 2022

@author: andreluizrodriguesdasilva
"""

# Match Statement in Python
# equivalent of the Java switch statement

color = "purple"

match color:
    case"red":
        print("The color is red")
    case "yellow":
        print("The color is yellow")
    case "blue":
        print("Blue like the sea...")
    case other_color:
        print("You chose a different color:", other_color)
        
        
# we can use the | operator to include multiple patterns in the same case:
match color:
    case "yellow" | "purple":
        print("Wow, you picked yellow or purple")
    case "blue":
        print("Blue like the sea...")
    case "red":
        print("Red here!")
        
        
        
# Matching Over Lists

my_list = [1, 2, 3]

match my_list:
    case [1, 2, 3]:
        print("contains 1, 2, 3")
    case [4, 5]:
        print("Contains 4 and 5")
    case _:
        print("No match")
        
        
        
match l:
    case [head, *tail]:
        print("First is", head)
        
    def recursive_sum(my_list):
    """Calculate the sum of the elements with pattern matching"""
        match my_list:
            case []:
                return 0
            case [head, *tail]:
                return head + recursive_sum(tail)
            
            
# Conditional Cases

num = 5
match num:
    case 0:
        print("It is zero")
    case n if n<100:
        print(n, "less than 100 but bigger than zero")
    case _:
        print("A really big number")
        

# custom classes in the match statement

class ButtonClicked:
    def __init__(self, mouse_button: str, x: int, y: int):
        self.x = x
        self.y = y
        self.mouse_button = mouse_button
        
b = ButtonClicked("left", 3, 5)
match b:
    case ButtonClicked(mouse_button="left"):
        print("Left mouse clicked at", b.x, b.y)
    case ButtonClicked(mouse_button="right"):
        print("Right mouse clicked at", b.x, b.y)
