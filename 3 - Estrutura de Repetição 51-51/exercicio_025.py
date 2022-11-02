"""
Eliezer Silva
Exercício 25
-------------
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se
a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma
é jovem, adulta ou idosa, conforme a média calculada.
"""

print()

quantidade = int(input('Escolha a quantidade de pessoas a serem inseridas: '))
cont = 0
idade = 0
turma = ''

for i in range(quantidade):
    idade += int(input(f'Digite a idade da pessoa {cont+1}: '))
    cont += 1

print(f'A média das idades inseridas é: {idade/cont:.2f} anos')

if idade/cont < 26:
    turma = 'jovem'
if 26 < idade/cont < 60:
    turma = 'adulta'
if idade/cont > 60:
    turma = 'idosa'

print(f'A turma informada é {turma}')
