"""
Eliezer Silva
Exercício 20
-------------
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
limitando o fatorial a números inteiros positivos e menores que 16.
"""

print('Escolha um valor entre 2 e 16.')
print()


def fatorial():
    numero = int(input("Fatorial de: "))

    if numero < 0 or numero > 16:
        print('Escolha para fatorial entre 2 e 16.')
        print()
        fatorial()

    resultado = 1
    contador = 1

    while contador <= numero:
        resultado *= contador
        contador += 1

    print(resultado)

    def continuar():
        continua = input('Deseja fatorial outro número [s/n]: ')
        if continua == 's':
            print()
            fatorial()
        if continua == 'n':
            print()
            print('Finalizando...')
            quit()

    continuar()


fatorial()
