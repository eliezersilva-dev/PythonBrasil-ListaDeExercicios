"""
Eliezer Silva
Exercício 21
-------------
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

numero = int(input('Digite um número: '))

if numero > 1:

    for i in range(2, numero, 1):

        if numero % i == 0:
            print(f'O número {numero} não é primo')
            break
    else:
        print(f'O número {numero} é primo')

else:
    print(f'O número {numero} é primo...')
