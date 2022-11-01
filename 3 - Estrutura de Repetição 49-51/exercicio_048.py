"""
Eliezer Silva
Exercício 48
-------------
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
"""

print()
numero = input('Digite um inteiro positivo: ')
numero = numero[::-1]
print(f'=> {numero}')
