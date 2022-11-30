"""
Eliezer Silva
Exercício 05
-------------
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
números IMPARES no vetor impar. Imprima os três vetores.
"""

import random

print()
numeros = []
cont = 1

while cont <= 20:
    numeros.append(random.randrange(1, 99, 1))
    cont += 1

par = []
impar = []

for i in numeros:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'Vetor: {numeros}\n'
      f'Par: {par}\n'
      f'Impar: {impar}')
