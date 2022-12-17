"""
Eliezer Silva
Exercício 04
-------------
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""
print()


def funcao(numero):
    if numero >= 1:
        print('P')
    else:
        print('N')


valor = int(input('Digite um valor: '))


funcao(numero=valor)
