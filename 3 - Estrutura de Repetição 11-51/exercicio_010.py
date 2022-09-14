"""
Eliezer Silva
Exercício 10
-------------
Faça um programa que receba dois números inteiros e gere os
números inteiros que estão no intervalo compreendido por eles.
"""

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

lista = [valor1, valor2]
intervalo = list(range(lista[0], lista[1], 1))

intervalo.remove(lista[0])
print(intervalo)
