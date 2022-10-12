"""
Eliezer Silva
Exercício 07
-------------
Faça um programa que leia 5 números e informe o maior número.
"""

print()
print('-' * 10 + ' Maior número ' + '-' * 10)
print()

print('Digite cinco números.')
print()

valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo número: '))
valor3 = int(input('Digite o terceiro número: '))
valor4 = int(input('Digite o quarto número: '))
valor5 = int(input('Digite o quinto número: '))

lista = [valor1, valor2, valor3, valor4, valor5]

print(f'O maior número digitado foi: {max(lista)}')
