"""
Eliezer Silva
Exercício 03
-------------
Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
F
U
L
A
N
O
"""
print()

nome = input('Digite um nome: ')
nome = nome.upper()

for i in nome:
    print(i)
