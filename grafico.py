#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 12:00:40 2022

@author: andreluizrodriguesdasilva
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

# ---------------------------------------------------------------------------------
#                           MONTE-CARLO
# ---------------------------------------------------------------------------------
# Calcula o payoff da opção de compra (GBM - Movimento Browniano Geométrico)
def payoff_call(S0, r, T, vol, K1_call, K2_call):
    S= S0*math.exp((r - 0.5*vol**2)*T + vol*((T)**0.5)*np.random.normal(0, 1))
    pay1_call = max(0, S - K1_call) # calcula o payoff
    pay2_call = max(0, S - K2_call)
    return S, pay1_call, pay2_call  # saída da função

#  Calcula o payoff da opção de venda(GBM - Movimento Browniano Geométrico)
def payoff_put(S0, r, T, vol, K1_put, K2_put):
    S= S0*math.exp((r - 0.5*vol**2)*T + vol*((T)**0.5)*np.random.normal(0, 1))
    pay1_put = max(0, S - K1_put)   # calcula o payoff
    pay2_put = max(0, S - K2_put)
    return S, pay1_put, pay2_put    # calcula o payoff

# Parâmetros
nSim = 10000 # N° de simulações
S0 = 32      # Spot inicial
K1_call = 40 # Strike
K2_call = 30
K1_put = 40
K2_put = 30
r = 0.018    # Taxa livre de risco
vol = 0.15   # volatilidade
T = 1        # prazo anualizado

# Dataframe p/ colocar as saídas da simulação
dfOpcao_c = pd.DataFrame(np.zeros((int(nSim), 3)), columns=['Spot', 'Payoff_call_1', 'Payoff_call_2']) # dataframe c/ n° de nSim linhas
for i in range(len(dfOpcao_c)): # rodo o laço em todas as simualações que quero fazer
    if i%10000 == 0: # print só para mostrar que está rodando
        print('Estou na simulação n° ' + str(i))
    dfOpcao_c['Spot'].iloc[i], dfOpcao_c['Payoff_call_1'].iloc[i], dfOpcao_c['Payoff_call_2'].iloc[i] = payoff_call(S0, r, T, vol, K1_call, K2_call) # salvo o spot e o payoff nas colunas adequadas
        
call_1 = dfOpcao_c['Payoff_call_1'].mean()/math.exp(r*T)
print(' preço de minha opção de compra é de ' + str(call_1) + ' dinheiros.')

call_2 = dfOpcao_c['Payoff_call_2'].mean()/math.exp(r*T)
print(' preço de minha opção de compra é de ' + str(call_2) + ' dinheiros.')

# c(K1) - c*(K2), K1 > K2
dif_c_k1_maior_k2 = call_1 - call_2

# Gráfico
dfOpcao_c['Dif_K1>K2'] = dfOpcao_c.apply(lambda x:(x['Payoff_call_1'] - x['Payoff_call_2']), axis = 1) 

fig, ax = plt.subplots()
ax.grid()

ax.scatter(dfOpcao_c['Spot'], dfOpcao_c['Dif_K1>K2'], color = 'red')
plt.show()

# c(K1) - c(K2), K1 < K2
# troca
call_1, call_2 = call_2, call_1

dif_c_k1_menor_k2 = call_1 - call_2

# Gráfico
dfOpcao_c['Dif_K1<K2'] = dfOpcao_c.apply(lambda x:(x['Payoff_call_1'] - x['Payoff_call_2']), axis = 1) 

fig, ax = plt.subplots()
ax.grid()

ax.scatter(dfOpcao_c['Spot'], dfOpcao_c['Dif_K1<K2'], color = 'red')
plt.show()


# Dataframe p/ colocar as saídas da simulação
dfOpcao_p = pd.DataFrame(np.zeros((int(nSim), 3)), columns=['Spot', 'Payoff_put_1', 'Payoff_put_2']) # dataframe c/ n° de nSim linhas
for i in range(len(dfOpcao_p)): # rodo o laço em todas as simualações que quero fazer
    if i%10000 == 0: # print só para mostrar que está rodando
        print('Estou na simulação n° ' + str(i))
    dfOpcao_p['Spot'].iloc[i], dfOpcao_p['Payoff_put_1'].iloc[i], dfOpcao_p['Payoff_put_2'].iloc[i] = payoff_put(S0, r, T, vol, K1_put, K2_put) # salvo o spot e o payoff nas colunas adequadas
        
put_1 = dfOpcao_p['Payoff_put_1'].mean()/math.exp(r*T)
print(' preço de minha opção de compra é de ' + str(call_1) + ' dinheiros.')

put_2 = dfOpcao_p['Payoff_put_2'].mean()/math.exp(r*T)
print(' preço de minha opção de compra é de ' + str(call_2) + ' dinheiros.')

# c(K1) - c*(K2), K1 > K2
dif_p_k1_maior_k2 = put_1 - put_2

# Gráfico
dfOpcao_p['Dif_K1>K2'] = dfOpcao_p.apply(lambda x:(x['Payoff_put_1'] - x['Payoff_put_2']), axis = 1) 

fig, ax = plt.subplots()
ax.grid()

ax.scatter(dfOpcao_p['Spot'], dfOpcao_p['Dif_K1>K2'], color = 'red')
plt.show()

# c(K1) - c(K2), K1 < K2
# troca
put_1, put_2 = put_2, put_1

dif_p_k1_menor_k2 = put_1 - put_2

# Gráfico
dfOpcao_p['Dif_K1<K2'] = dfOpcao_p.apply(lambda x:(x['Payoff_put_1'] - x['Payoff_put_2']), axis = 1) 

fig, ax = plt.subplots()
ax.grid()

ax.scatter(dfOpcao_p['Spot'], dfOpcao_p['Dif_K1<K2'], color = 'red')
plt.show()

