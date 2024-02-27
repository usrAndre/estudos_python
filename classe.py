#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 15:05:29 2022

@author: andreluizrodriguesdasilva
"""

class Veiculo:
    def __init__(self, marca, cor, motorLigado):
        self.__marca = marca
        self.__cor = cor
        self.__motorLigado = motorLigado
    def getMarca(self):
        return self.__marca
    def getCor(self):
        return self.__cor
    def isMotorLigado(self):
        return self.__motorLigado
    def ligaMotor(self):
        if self.__motorLigado == True:
            print('O motor já está ligado!')
        else:
            self.__motorLigado = True
            print('O motor acaba de ser ligado!')
            
class Motocicleta(Veiculo):
    # construtor
    def __init__(self, marca, cor, motorLigado, estilo):
        # chama construtor da super classe
        super().__init__(marca, cor, motorLigado)
        self.__estilo = estilo
    def getEstilo(self):
        return self.__estilo
    # método de instância
    def mostraAtributos(self):
        print('Esta motocicleta é uma {} {} estilo {}'.format
        (self.getMarca(), self.getCor(), self.getEstilo()))
        if(self.isMotorLigado()):
            print('Seu motor está ligado')
        else:
            print('Seu motor está desligado')

class Carro(Veiculo):
    def __init__(self, marca, cor, motorLigado, portaMalasCheio):
    # chama construtor da super classe
        super().__init__(marca, cor, motorLigado)
        self.__portaMalasCheio = portaMalasCheio
    def isPortaMalasCheio(self):
        return self.__portaMalasCheio
    def enchePortaMalas(self):
        if self.__portaMalasCheio == True:
            print('O porta malas já está cheio!')
        else:
            self.__portaMalasCheio = True
            print('O porta malas acaba de ser carregado!')
    def mostraAtributos(self):
        print('Este carro é um {} {}'.format(self.getMarca(), self.
        getCor()))
        if(self.isMotorLigado()):
            print('Seu motor está ligado')
        else:
           print('Seu motor está desligado')
        if(self.isPortaMalasCheio()):
            print('Seu porta malas está cheio')
        else:
            print('Seu porta malas está vazio')
            
    
    
m = Motocicleta('Honda', 'azul', False, 'naked')
m.mostraAtributos()
m.ligaMotor()
m.mostraAtributos()
print('-----------')
c = Carro('Chevrolet', 'branco', False, False)
c.mostraAtributos()
c.enchePortaMalas()
c.ligaMotor()
c.mostraAtributos()