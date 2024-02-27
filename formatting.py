#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:11:28 2022

@author: andreluizrodriguesdasilva
"""

#import pandas as pd

# formatting f'{}'

# :b , converte número em binário
print(f'Binary for 10 is: {10:b}')
print(f'Binary for 23 is: {23:b}')

# :< , alinha à esquerda c/ espaço especificado, no ex. 10
print(f'Python {"is":<10} easy')

# :< , alinha ao centro c/ espaço especificado, no ex. 10
print(f'Python {"is":^10} easy')

# :< , alinha à direita c/ espaço especificado, no ex. 10
print(f'Python {"is":>10} easy')


# :% formato de porcentagem, no ex. .2% significa c/ 2 casas decimais
print(f'Your score is {0.7515:.2%}')

# :% formato de porcentagem, no ex. .0% significa c/ 0 casas decimais
print(f'Your score is {0.75:.0%}')


# , (vírgula) como separador de milhar
print(f'{1000000:,}')

