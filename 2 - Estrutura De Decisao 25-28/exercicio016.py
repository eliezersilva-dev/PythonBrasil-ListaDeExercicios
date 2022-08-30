"""
Eliezer Silva
Exercício 16
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais
valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

import math

print()
print('*'*10+' Cálculo de Equação de 2º Grau '+'*'*10)
print()

print('Equaçao do 2o grau da forma: ax² + bx + c')
print()

a = int(input('Informe o Coeficiente a: '))

if a == 0:
    print('Se a = 0, não é equação do segundo grau.')
else:
    b = int(input('Informe o Coeficiente b: '))
    c = int(input('Informe o Coeficiente c: '))
    delta = b * b - (4 * a * c)

    if delta < 0:
        print('Delta negativo. A equação não possui raiz real. \n'
              'Programa encerrado.')
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f'Delta igual a 0 , a equação possui apenas uma raiz = {raiz}')
    else:
        raiz_1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz_2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f' A equação possui duas raizes: {raiz_1} e {raiz_2}')
