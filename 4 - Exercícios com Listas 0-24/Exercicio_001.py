"""
Eliezer Silva
Exercício 01
------------
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

obs: Python é uma linguagem de programação de alto nível e tipagem dinâmica, sendo assim não há
necessidade de pré definir o tamanho do seu vetor, como é feito em C por exemplo (int vetor[5]={1, 2, 3, 4, 5}).
"""
import random
vetor = []
cont = 1
while cont <= 5:
    vetor.append(random.randrange(1, 99, 1))
    cont += 1
print(f'Vetor: {vetor}')
