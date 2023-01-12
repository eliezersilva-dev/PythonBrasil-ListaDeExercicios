"""
Eliezer Silva
Exercício 02
-------------
Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre
o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o
usuário pode digitar letras maiúsculas ou minúsculas.
"""
import string

print()

nome = input('Digite um nome: ')

nome_maiusculo = nome.upper()
print(f'Nome em letras maiúsculas: {nome_maiusculo}')
nome_inverso = nome_maiusculo[::-1]
print(f'Nome de trás para frente: {nome_inverso}')
