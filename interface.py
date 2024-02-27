#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 15:35:10 2022

@author: andreluizrodriguesdasilva
"""

import tkinter as tk

def main():
    # Cria a janela
    janela = tk.Tk()
    janela.title('Primeira janela')
    
    # Entrra no mainloop, o que faz com que
    # a janela seja renderizada na tela
    janela.mainloop()
    
main()


'''LABEL'''
# Usando classes p/ criar interfaces
import tkinter as tk

class GUI:
    def __init__(self):
        # Cria a janela
        self.janela = tk.Tk()
        # Note que a janela é passada como argumento
        self.label = tk.Label(self.janela, text='Hello world')
        # Chama o método pack()
        self.label.pack()
        self.janela.mainloop()

def main():
   GUI()
        
main()

'''
# Ajustando o tamanho da fonte
self.label = tk.Label(self.janela,
             text='Hello world',
             font=('Arial Bold', 50))
'''
