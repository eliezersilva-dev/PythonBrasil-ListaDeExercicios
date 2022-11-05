"""
Eliezer Silva
Exercício 02
-------------
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

import random
print()
vetor = []
cont = 1
while cont <= 10:
    vetor.append(random.randrange(1, 99, 1))
    cont += 1

print(f'Vetor: {vetor}')
print(f'Vetor invertido: {list(reversed(vetor))}')
