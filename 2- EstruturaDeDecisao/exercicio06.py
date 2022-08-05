"""
Eliezer Silva
Exercício 06
Faça um Programa que leia três números e mostre o maior deles.
"""

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

lista = n1, n2, n3
lista = list(lista)

lista.sort()
print(f'O maior número informado foi {lista[-1]}')
