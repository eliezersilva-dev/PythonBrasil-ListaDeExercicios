"""
Eliezer Silva
Exercício 09
-------------
Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor.
"""
import random

print()

vetorA = []
vetorA_quadrado = []
vetorA_soma = []
cont = 1

while cont <= 10:
    vetorA.append(random.randint(1, 99))
    cont += 1
print(f'Vetor A: {vetorA}')

for i in vetorA:
    vetorA_quadrado.append(i ** 2)
print(f'Elementos Vetor A ao quadrado: {vetorA_quadrado}')

vetorA_soma = sum(vetorA_quadrado)
print(f'Soma dos quadrados dos elementos do Vetor A: [{vetorA_soma}]')
