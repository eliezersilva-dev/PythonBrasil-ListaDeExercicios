"""
Eliezer Silva
Exercício 07
------------
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""
import random

print()

vetor = []
cont = 1

while cont <= 5:
    vetor.append(random.randint(1, 99))
    cont += 1

numeros = str(vetor)
numeros = numeros.replace('[', '')
numeros = numeros.replace(']', '')
print(f'Números: {numeros}')

soma = sum(vetor)
print(f'Soma dos números: {soma}')

multiplicao = 1
for i in vetor:
    multiplicao *= i

print(f'Multiplicação dos números: {multiplicao}')
