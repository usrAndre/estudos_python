#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:45:35 2022

@author: andreluizrodriguesdasilva
"""

# analisa o argumento da expressão e o avalia como uma expressãp python
# eval(expression, [globals[,locals]])

x = 2
eval('x+5')


# argumentos de eval(): string, globals e locals são opcionais
# globals devem ser do tipo dicionário e locals de qualquer tipo
# se globals for fornecido s/ vaor da chave, uma referência é gerada
# p/ o dicionário do módulo integrado builtins e inserida na chave antes
# que a expressãp comece a analisar.
''' EXEMPLO'''
# lista c/ o número de núcleos disponíveis dentro do sistema

from os import cpu_count
eval('[1,cpu_count()]')
