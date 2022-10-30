"""
Eliezer Silva
Exercício 15
-------------
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

lista = [0, 1, 1]


def fibonacci():
    variavel = lista[-1] + lista[-2]
    lista.append(variavel)
    print(lista)
    print()
    continuar()


def continuar():
    continua = input('Deseja continuar? [s/n]')
    if continua == 's':
        fibonacci()
    if continua == 'n':
        print('Finalizando...')
        quit()


fibonacci()
