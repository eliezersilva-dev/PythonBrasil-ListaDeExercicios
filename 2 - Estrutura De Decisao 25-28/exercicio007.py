"""
Eliezer Silva
Exercício 07
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

lista = n1, n2, n3
lista = list(lista)

lista.sort()
print(f'O maior número informado foi: {lista[-1]}')
print(f'O menor número informado foi: {lista[0]}')
