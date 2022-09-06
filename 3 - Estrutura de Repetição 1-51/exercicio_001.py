"""
Eliezer Silva
Exercício 01
_____________
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido
e continue pedindo até que o usuário informe um valor válido.
"""

print()
print('-' * 10 + ' Notas válidas ' + '-' * 10)
print()

nota = ''
validacao = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


def valida():
    nota = input('Digite uma nota entre 0 e 10: ')
    if nota in validacao:
        print(f'Valor digitado {nota} é válido.')
        quit()
    else:
        print(f'Valor digitado {nota} não é válido.\n'
              f'Tente novamente.')
        print()
        valida()


valida()
