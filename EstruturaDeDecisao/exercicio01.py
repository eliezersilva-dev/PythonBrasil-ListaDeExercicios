"""
Eliezer Silva
Exercício 01
Faça um Programa que peça dois números e imprima o maior deles.
"""

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

if numero1 > numero2:
    print(f'Os números digitados foram {numero1} e {numero2} sendo o maoir deles o {numero1}.')
if numero1 < numero2:
    print(f'Os números digitados foram {numero1} e {numero2} sendo o maoir deles o {numero2}.')
