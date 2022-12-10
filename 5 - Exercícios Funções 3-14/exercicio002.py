"""
Eliezer Silva
Exercício 02
-------------
Faça um programa para imprimir:

    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n

Para um n informado pelo usuário.
Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""
print()


def funcao():
    numero = int(input('Digite um número: '))
    lista = list(range(1, numero + 1, 1))

    for i in lista:
        for j in range(1, i + 1):
            print(j, end='  ')
        print('')


funcao()
