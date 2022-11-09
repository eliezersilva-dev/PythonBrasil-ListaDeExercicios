"""
Eliezer Silva
Exercício 10
-------------
Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser
compostos pelos elementos intercalados dos dois outros vetores.
"""

vetor_um = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
vetor_dois = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K']


print(f'Vetor Um: {vetor_um[::1]}')
print(f'Vetor Dois: {vetor_dois[::1]}')

vetor_tres = vetor_um + vetor_dois
vetor_tres[::2] = vetor_um
vetor_tres[1::2] = vetor_dois

print(f'Vetor Três: {vetor_tres}')
