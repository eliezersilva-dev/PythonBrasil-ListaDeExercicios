"""
Eliezer Silva
Exercício 14
-------------
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números impares.
"""

print()
print('-' * 10 + ' Par ou Impar ' + '-' * 10)
print()

print('Digite dez valores.')
print()

lista = []

lista.append(int(input('Valor 1: ')))
lista.append(int(input('Valor 2: ')))
lista.append(int(input('Valor 3: ')))
lista.append(int(input('Valor 4: ')))
lista.append(int(input('Valor 5: ')))
lista.append(int(input('Valor 6: ')))
lista.append(int(input('Valor 7: ')))
lista.append(int(input('Valor 8: ')))
lista.append(int(input('Valor 9: ')))
lista.append(int(input('Valor 10: ')))

par = []
impar = []

for i in lista:
    if i % 2 == 0:
        par.append(i)
    if i % 2 != 0:
        impar.append(i)

quantidade_par = len(par)
quantidade_impar = len(impar)

print()
print(f'O números digitados foram: {lista}')
print(f'Quantidade de números pares: {quantidade_par}')
print(f'Quantidade números impares: {quantidade_impar}')
