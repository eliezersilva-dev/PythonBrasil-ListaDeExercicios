"""
Eliezer Silva
Exercício 22

Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).
"""

print()
print('-'*10 + ' Par ou Impar ' + '-'*10)
print()

try:
    numero = int(input('Digite um número inteiro: '))

    if numero % 2 == 0:
        print(f'O número {numero} é PAR')
    else:
        print(f'O número {numero} é IMPAR.')
except:
    print('error: Digite um valor válido.')




