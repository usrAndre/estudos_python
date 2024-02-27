#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:01:33 2022

@author: andreluizrodriguesdasilva
"""


# several alternative methods by which we can implement Switch Case statements in python.
'''
1. With help of dictionaries

    By using functions

    By using Lambdas

2. With help of classes

3. With help of if-elif-else statements
'''


# Python Switch Case Using Functions
def one():
    return "one"
def two():
    return "two"
def three():
    return "three"
def four():
    return "four"
def five():
    return "five"
def six():
    return "six"
def seven():
    return "seven"
def eight():
    return "eight"
def nine():
    return "nine"
def default():
    return "no spell exist"

numberSpell = {
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven,
    8: eight,
    9: nine
    }

def spellFunction(number):
    return numberSpell.get(number, default)()

print(spellFunction(3))
print(spellFunction(10))


# Python Switch Case Using Lambdas
def one():
    return "one"
def two():
    return "two"
def three():
    return "three"

def spellFunction(number):
    numberSpell = {
        1: one,
        2: two,
        3: three,
        4: lambda: "four"
    }

    return numberSpell.get(number, lambda: "no number spell exist")()

print(spellFunction(1))
print(spellFunction(7))


# Switch Case using Python Classes
'''
We have to use getattr function which is used for implementing of switch case by using classes. Let's understand in brief about this function.
'''
# syntax:
# getattr(object, name, default)

'''
This is the syntax of getattr which is accepts 3 parameters object, name and default. All the 3 parameters are explained below. Read along to know more.
Parameters

Getattr accepts 3 parameter which is used for implementation of conditional statement(switch case) using classes. These parameters are:

    1. object(MANDATORY PARAMETER): object name whose attribute is to be returned.
    2. name(MANDATORY PARAMETER): string that contains the attribute name of the object.
    3. default(OPTIONAL PARAMETER): if the attribute is not present in object then default statement is returned.

'''
# Example
class binaryOrNot():
    def mainFunction(self,i):
            method_name='binary_'+str(i)
            method = getattr(self,method_name,lambda: 'not a binary digit')
            return method()
    def binary_0(self):
            return 'zero'
    def binary_1(self):
            return 'one'
binary=binaryOrNot()
print(binary.mainFunction(1))


# Python Switch Case using if-elif-else
number = 15

if(number < 0):
    print('number is a negative number')
elif(1 <= number <= 10):
    print('number lies in between of 1 and 10')
else:
    print('number is greater than 10')


# Application of Switch Case in Python
print('Welcome to Scaler Academy')
print('1. visit python hub')
print('2. visit dsa hub')
print('3. visit java hub')
print('4. more')

print('input the suitable option in the next line:')
textInput = int(input())

if(textInput == 1):
    print('Thank you. We are redirecting to python hub.')

elif(textInput == 2):
    print('Thank you. We are redirecting to dsa hub.')

elif(textInput == 3):
    print('Thank you. We are redirecting to java hub.')

elif(textInput == 4):
    print('Thank you. We are redirecting to more section.')
else:
    print('wrong input')


########################################################################################

# Geek for Geeks
def number_to_string(argument):
	match argument:
		case 0:
			return "zero"
		case 1:
			return "one"
		case 2:
			return "two"
		case default:
			return "something"


if __name__ = "__main__":
	argument = 0
	number_to_string(argument)
