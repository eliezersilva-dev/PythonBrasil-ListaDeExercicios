"""
Eliezer Silva
Exercício 24
-------------

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""

print()
print('-' * 10 + ' Inteiro ou Decimal ' + '-' * 10)
print()



try:

    numero1 = float(input('Digite um número: '))
    numero2 = float(input('Digite outro número: '))


    operacao = input('Escolha uma operação:\n'
                     'Para soma digite [+]\n'
                     'Para subtração digite [-]\n'
                     'Para multiplicação digite [*]\n'
                     'Para divisão digite [/]\n'
                     'Escolha: ')

    print()
    resultado = 0

    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    elif operacao == '/':
        resultado = numero1 / numero2
    else:
        print('Operação inválida.')
        quit()
    print(f'{numero1} {operacao} {numero2} = {resultado:.2f}')

    if resultado % 2 == 0:
        print(f'{resultado:.2f} é um número par.')
    else:
        print(f'{resultado:.2f} é um número impar. ')

    if resultado >= 0:
        print('É também um número positivo.')
    else:
        print('É também um número positivo.')

    if resultado == round(resultado):
        print('E ainda é um número inteiro.')
    else:
        print('E ainda não é um número inteiro.')

except ZeroDivisionError as error:
    print(f'Erro: {error} - Não se divide por zero')

except:
    print('Erro. Tente novamente.')
