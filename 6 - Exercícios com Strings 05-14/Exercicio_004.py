"""
Eliezer Silva
Exercício 04
-------------
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
F
FU
FUL
FULA
FULAN
FULANO
"""
print()

nome = input('Digite um nome: ')
nome = nome.upper()
n = 1

for i in nome:
    print(nome[0:n:])
    n += 1
