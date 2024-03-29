#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 18:14:26 2022

@author: andreluizrodriguesdasilva
"""

import tkinter as tk

class MyGUI:
    def __init__(self):
        # Cria a janela
        self.janela = tk.Tk()
        
        # Cria dois frames, um para o topo da janela
        # e outro para a base da janela
        self.frameTopo = tk.Frame(self.janela)
        self.frameBase = tk.Frame(self.janela)
        
        # Cria 3 labels para o frame do topo
        self.label1 = tk.Label(self.frameTopo, text='Um')
        self.label2 = tk.Label(self.frameTopo, text='Dois')
        self.label3 = tk.Label(self.frameTopo, text='Três')
        
        # Empacota os labels do frame do topo
        # Use side='top' para empilhar labels
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')
        
        # Cria 3 labels para o frame da base
        self.label4 = tk.Label(self.frameTopo, text='Um')
        self.label5 = tk.Label(self.frameTopo, text='Dois')
        self.label6 = tk.Label(self.frameTopo, text='Três')
        
        # Empacota os labels do frame da base
        # Use side='left' para empilhar labels
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')
        
        # Finalmente empacota os frames
        self.frameTopo.pack()
        self.frameBase.pack()
        
        # Entra no mainloop
        self.janela.mainloop()
        
def main():
    MyGUI()
    
main()