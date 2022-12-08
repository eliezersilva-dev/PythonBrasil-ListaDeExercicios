"""
Eliezer Silva
Exercício 01
-------------
Faça um programa para imprimir:

    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
"""
print()

numero = int(input('Digite um número: '))
lista = list(range(1, numero+1, 1))
for i in lista:
    print(i * str(i))
