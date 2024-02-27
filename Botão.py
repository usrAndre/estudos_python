#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 18:32:31 2022

@author: andreluizrodriguesdasilva
"""

import tkinter as tk

class MyGUI:
    def __init__(self):
        self.janela = tk.Tk()
        
        # Criando 2 botões
        self.botao1 = tk.Button(self.janela, \
                                text='Botão 1', \
                                command=self.processaB1)
        self.botao2 = tk.Button(self.janela, \
                                text='Botão 2', \
                                command=self.processaB2)
            
        self.botao1.pack()
        self.botao2.pack()
        
        self.label = tk.Label(self.janela, text='Escolha ...')
        self.label.pack()            
        
        # Entra no mainloop
        tk.mainloop()
        
    # Define as funções de callbak
    def processaB1(self):
        self.label.configure(text='Botão 1 foi clicado')
    def processaB2(self):
        self.label.configure(text='Botão 2 foi clicado')
        
def main():
    MyGUI()
    
main()