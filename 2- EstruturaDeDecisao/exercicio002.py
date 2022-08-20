"""
Eliezer Silva
Exercício 02
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

numero = float(input('Digite um número: '))
if numero < 0:
    print(f'O número {numero} é negativo.')
else:
    print(f'O número {numero} não é negativo.')
