"""
Eliezer Silva
Exercício 34
-------------
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo.
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
"""
print()


def numero_primo():

    def continua():
        repetir = input('Repetir? [s/n]: ')
        if repetir == 'n':
            print('bye...')
            quit()
        if repetir == 's':
            print()
            numero_primo()


    numero = int(input('Digite um numero inteiro: '))
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            print(f'{numero} não é primo!')
            continua()
    if primo:
        print(f'{numero} é primo!')
        continua()

numero_primo()
