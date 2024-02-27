#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 12:56:57 2022

@author: andreluizrodriguesdasilva
"""

from abc import ABC, abstractmethod

class Documento(ABC):
    def __init__(self, nome): # São um ESPAÇO e dois underlines SEMPRE
        self.__nome = nome
        
    def getNome(self):
        return self.__nome
    
    @abstractmethod
    def visualizar(self):
        pass

class Pdf(Documento):
    def visualizar(self):
        return 'Mostra no Adobe Acrobat'
    
class Word(Documento):
    def visualizar(self):
        return 'Mostra no Word'
        
documentos = [Pdf('PDF1'), Word('DOC1'), Pdf('PDF2')]
for documento in documentos:
    print('{}: {}'.format(documento.getNome(), documento.visualizar()))    
        