#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 10:53:49 2022

@author: andreluizrodriguesdasilva
"""

class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # Método da instância
    '''def description(self):
        return f"{self.name} is {self.age} years old"'''
    
    # usando método __str__(self)
    def __str__(self): # consegue c/ print(miles) imprimir as informações de instanciancia 
        return f"{self.name} is {self.age} years old"
    
    # Outro método da instância
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    
    
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):  # NÃO consegue c/ print(miles) imprimir as informações de instanciancia 
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"
    

class JackRusselTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass


# isinstance(miles, Dog)


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)