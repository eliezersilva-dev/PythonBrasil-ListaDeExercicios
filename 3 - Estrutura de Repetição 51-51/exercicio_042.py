"""
Eliezer Silva
Exercício 42
-------------
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos
deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados
deverá terminar quando for lido um número negativo.
"""

print()


lista = []
qtda_numeros = int(input('Quantos números deseja inserir? '))

numero_cont = 1
while qtda_numeros > 0:
    numero = (int(input(f'Insira o número {numero_cont}: ')))
    if numero < 0:
        print('Insira um número positivo.')
        quit()
    lista.append(numero)
    qtda_numeros -= 1
    numero_cont += 1

print()

cont1 = 0
for i in range(0, 25):
    for j in lista:
        if i == j:
            cont1 += 1
print(f'No intervalo entre [0-25] os números digitados aparecem {cont1} vezes.')

cont2 = 0
for i in range(26, 50):
    for j in lista:
        if i == j:
            cont2 += 1
print(f'No intervalo entre [26-50] os números digitados aparecem {cont2} vezes.')

cont3 = 0
for i in range(51, 75):
    for j in lista:
        if i == j:
            cont3 += 1
print(f'No intervalo entre [51-75] os números digitados aparecem {cont3} vezes.')

cont4 = 0
for i in range(76, 100):
    for j in lista:
        if i == j:
            cont4 += 1
print(f'No intervalo entre [76-100] os números digitados aparecem {cont4} vezes.')

