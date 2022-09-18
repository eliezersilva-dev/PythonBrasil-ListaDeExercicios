"""
Eliezer Silva
Exercício 16
-------------
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500
"""
import time

lista = [0, 1, 1]


def fibonacci():
    variavel = lista[-1] + lista[-2]
    lista.append(variavel)
    time.sleep(1.2)
    print(lista)

    if lista[-1] < 500:
        fibonacci()

    print()


fibonacci()
