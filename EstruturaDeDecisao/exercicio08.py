"""
Eliezer Silva
Exercício 08
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""

preco1 = float(input('Informe o preço do produto A: '))
preco2 = float(input('Informe o preço do produto B: '))
preco3 = float(input('Informe o preço do produto C: '))

lista = [['A', preco1], ['B', preco2], ['C', preco3]]

lista.sort(key=lambda i: i[1])  # Usando expressão lambda para retornar o índice 1 de cada ítem da lista e ordenar com sort

print(f'Você deve comprar o produto {lista[0][0]}')

