#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 17:13:20 2022

@author: andreluizrodriguesdasilva
"""
# Dicionário
pessoa = {'nome':'Pedro'}
pessoa['sobrenome'] = 'Souza'
print(pessoa)
print(pessoa['nome'])
print(pessoa['sobrenome'])


# Iteração controlado por uma condição
nomes = ['Pedro', 'Marina', 'Beto']
index = 0
while index < len(nomes):
    print(nomes[index])
    # Muda a condição
    index = index + 1
    
    
# Strings são listas de caracteres    
for x in 'Ana':
    print(x)
    
    
# Função p/ retornar a primeira letra de uma string
def get_inicial(str):
    inicial = str[0:1]
    return inicial

nome = input('Digite seu nome: ')
inicial_nome = get_inicial(nome)
sobrenome = input('Digite seu sobrenome: ')
inicial_sobrenome = get_inicial(sobrenome)

print('Suas iniciais são: '+inicial_nome+inicial_sobrenome)


# múltiplos parâmetros, com parâmetro default
def get_inicial(str, maiuscula=True):
    if maiuscula:
        inicial = str[0:1].lower()
    else:
        inicial = str[0:1]
    return inicial

nome = input('Digite seu nome: ')
inicial_nome = get_inicial(nome, False)
print('Sua inicial é: ' + inicial_nome)


# Parâmetros nomeados
def get_inicial(str, maiuscula):
    if maiuscula:
        inicial = str[0:1].upper()
    else:
        inicial = str[0:1]
    return inicial

'''Quando os parâmetros são nomeados,
 eles podem aparecer em qualquer ordem'''
 
nome = input('Digite seu nome: ')
inicial_nome = get_inicial(maiuscula=True, str=nome)
print('Sua inicial é: ' + inicial_nome)