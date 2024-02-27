#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 20:31:03 2022

@author: andreluizrodriguesdasilva
"""

class Retangulo:
    lado_a = None   # Opcional
    lado_b = None   # Opcional
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
        print("Criada uma nova instância Retangulo")
    def calcula_area(self):
        return self.lado_a * self.lado_b
    def calcula_perimetro(self):
        return 2 * self.lado_a + 2 * self.lado_b
    
obj = Retangulo(4, 6)
obj.lado_a
obj.lado_b
obj.calcula_area()
obj.calcula_perimetro()



class ContaCorrente:
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0
        
    def debitar(self, valor):
        self.saldo = self.saldo - valor
        
    def creditar(self, valor):
        self.saldo = self.saldo + valor
        
        
c = ContaCorrente('1234')
c.saldo

c.creditar(1000)
c.saldo

c.debitar(342)
c.saldo



class Pessoa:
    #nome = None
    #idade = None
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def getAnoNascimento(self, anoAtual):
        return anoAtual - self.idade
    
pessoa = Pessoa("Pedro", 21)
print(pessoa.getAnoNascimento(2013))



# ATRIBUTOS PÚBLICOS E PRIVADOS (ENCAPSALAMENTO)
class Teste1:
    a = 1   # atributo Público DA CLASSE Teste1
    __b = 2 # atributo Privado DA CLASSE Teste1
    
    
t1 = Teste1()
print(t1.a)
    


class Teste2(Teste1):
    __c = 3 # atributo Privado DA CLASSE Teste2
    def __init__(self):
        print self.a
        print self.__c
    
    
t2 = Teste2()

print(t2.__b)  # Erro, pois __b é privado a classe A
print(t2.__c)  # Erro, __c é um atributo privado, somente acessado pela classe