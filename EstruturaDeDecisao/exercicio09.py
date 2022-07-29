"""
Eliezer Silva
Exercício 09
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

lista = [numero1, numero2, numero3]
lista.sort(reverse=True)  # ordena (sort) e organiza em modo decrescente (reverse=True)

print(*lista)  # '*' desempacota lista

