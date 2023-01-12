"""
Eliezer Silva
Exercício 05
-------------
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
"""
print()

nome = input('Digite um nome: ')
nome = nome.upper()
n = len(nome)

for i in nome:
    print(nome[0:n:])
    n -= 1
