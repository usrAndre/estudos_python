#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 12:17:02 2022

@author: andreluizrodriguesdasilva
"""

# importar module sys p/ pegar o tipo da exception
import sys

lista = ['a', 0, 2]

for elemento in lista:
    try:
        print('O elemento é ', elemento)
        r = 1/int(elemento)
        break
    except:
        print('Oops!', sys.exc_info()[0], 'ocorreu')
        print('Próxima entrada')
        print()
        
print('O número recíproco de', elemento, 'é', r)


''' Toda exceção em Python herda da classe base
Exception. Assim, o mesmo código pode ser escrito
da seguinte forma '''

lista = ['a', 0, 2]
for elemento in lista:
    try:
       print("O elemento é ", elemento)
       r = 1/int(elemento)
       break
    except Exception as e:
       print("Oops!", e.__class__, "ocorreu")
       print("Próxima entrada")
       print()
print("O número recíproco de", elemento , "é", r)


# imprime o número recíproco apenas de números pares
try:
    num = int(input("Digite um número: "))
    assert num % 2 == 0
except:
    print("Não é um número par!")
else:
    reciproco = 1/num
    print(reciproco)
    

# O try vai gerar uma exception ao tentar escrever num arquivo read-only
try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Algo saiu erra na operação de escrita")
finally:
    f.close()
# Finally será executado em qualquer situação, ou seja,
# ocorrendo ou não a exceção    



# É possível criar Exceptions definindo uma classe que
# herda da classe Exception
class ValorMenor(Exception):
    #Gerada quando o valor é menor
    pass
class ValorMaior(Exception):
    #Gerada quando o valor é maior
    pass
# número a ser descoberto
nro = 10

# usuário tenta adivinhar o número
while True:
    try:
        i_num = int(input("Digite um número: "))
        if i_num < nro:
            raise ValorMenor
        elif i_num > nro:
            ValorMaior
        break
    except ValorMenor:
        print("Valor menor, tente novamente!")
        print()
    except ValorMaior:
        print("Valor maior, tente novamente!")
        print()
        
print("Parabéns! Você descobriu o número.")