"""
Eliezer Silva
Exercício 03
-------------
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
import random
print()
notas = []
cont = 1
while cont <= 4:
    notas.append(random.randrange(1, 10, 1))
    cont += 1
media = sum(notas) / 4
print(f'Notas: {notas}\n'
      f'Média: {media:.2f}')
