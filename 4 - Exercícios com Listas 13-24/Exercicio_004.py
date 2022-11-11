"""
Eliezer Silva
Exercício 04
-------------
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""
import random
import string

print()

letras = string.ascii_uppercase
vetor = random.choices(letras, k=10)
print(vetor)

vogal = ['A', 'E', 'I', 'O', 'U']
consoante = []

for i in vetor:
    for j in vogal:
        if i == j:
            vetor.remove(i)

print(f'Foram encontradas {len(vetor)} consoantes.\n'
      f'São elas: {vetor}')
