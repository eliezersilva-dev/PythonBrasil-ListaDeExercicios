"""
Eliezer Silva
Exercício 03
-------------
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""
print()



def soma(num1, num2, num3):
    print(num1 + num2 + num3)


def insere_numeros():
    num1 = int(input('Insira o primeiro número: '))
    num2 = int(input('Insira o segundo número: '))
    num3 = int(input('Insira o terceiro número: '))
    soma(num1, num2, num3)


insere_numeros()
