#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 17:52:31 2022

@author: andreluizrodriguesdasilva
"""

# Assert
# estrutura do Python para depurar o código
'''
permitir verificar algumas condições para facilitar a correção de erros dentro do código'
'''

print('inicio')

assert 1 < 2

print('fim')

'''
Aqui nós vamos fazer uma verificação com o assert se 1 é menor do que 2. Como essa condição é verdadeira o código vai rodar normalmente.

Agora se essa condição for falsa, nós vamos ter um erro chamado AssertionError, que é para indicar que temos um erro exatamente no nosso assert.
'''
print('inicio')

assert 1 > 2

print('fim')


assert False == 1
assert True == 0

assert False == 0
assert True == 1

assert True == False

'''
Dessa forma vai saber exatamente onde está o erro e fica muito mais fácil corrigi-lo. Essa é uma estrutura do Python para depurar o código, então você não vai utilizá-la quando o código estiver de fato funcionando.
'''
# Para esse exemplo nós vamos utilizar a biblioteca requests (que é uma biblioteca de requisição).
import requests
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dic = requisicao.json()

cotacao = requisicao_dic["USDBRL"]['bid']
print(cotacao)

preco_produto = 100
assert type(cotacao) == float
faturamento = preco_produto * cotacao
print(faturamento)

'''
Teste prático com assert para verifica tipo de uma variável

Nesse exemplo nós estamos buscando na web a cotação do dólar e estamos colocando na tela para que você possa ver.

O valor aparece como 5.0797, mas ao utilizar o assert para verificar se o tipo dessa variável é float (número decimal) nós vamos ter um erro.

Isso acontece porque essa informação que estamos recebendo está no formato de texto e não no formato decimal.

Aqui é muito interessante você fazer essa verificação, pois quando for fazer qualquer operação com esse valor vai ter erro também pelo fato de o formato estar em texto.

Então você já garantindo que essa informação já está no formato correto já vai evitar vários erros em outras partes do seu código.

Outra verificação que pode fazer é se o valor é maior do que 0 por exemplo, pois dessa forma teríamos outro problema.

Então com o assert você vai se certificar de que as suas informações vão vir no formato correto e você já vai tratar essas informações para que fiquem corretas.

Dessa forma você evita erros futuros, erros de cálculos e até resultados errados no final do seu código!
'''