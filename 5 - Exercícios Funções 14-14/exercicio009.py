"""
Eliezer Silva
Execício 09
-------------
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""


def calcular_quantidade(numero):
    numero = str(numero)
    print(f'Quantidade de dígitos é de: {len(numero)}')


def insira_numero():
    numero = int(input('Insira um número inteiro: '))
    calcular_quantidade(numero=numero)


insira_numero()
