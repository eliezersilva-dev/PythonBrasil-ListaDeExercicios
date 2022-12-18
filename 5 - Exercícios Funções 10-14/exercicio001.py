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

Para um n informado pelo usuário.
Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""
print()


def funcao():
    numero = int(input('Digite um número: '))
    lista = list(range(1, numero + 1, 1))
    for i in lista:
        for j in range(i):
            print(i, end='  ')
        print('')


funcao()
