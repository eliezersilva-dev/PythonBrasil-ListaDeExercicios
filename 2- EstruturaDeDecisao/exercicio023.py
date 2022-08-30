"""
Eliezer Silva
Exercício 23
_____________
Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.
"""

print()
print('-'*10 + ' Inteiro ou Decimal ' + '-'*10)
print()

numero = float(input('Digite um número inteiro ou decimal: '))
num_round = round(numero)
print()

if numero == num_round:
    print(f'O número digitado é inteiro.')
else:
    print(f'O número digitado é decimal.')