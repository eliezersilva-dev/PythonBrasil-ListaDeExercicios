"""
Eliezer Silva
Exercício 24
-------------
Faça um programa que calcule o mostre a média aritmética de N notas.
"""
print()

quantidade = int(input('Escolha a quantidade de notas a ser inserida: '))
nota = 0
cont = 0

for i in range(quantidade):
    nota += int(input(f'Digite a nota {cont+1}: '))
    cont += 1

print(f'A média das notas inserida é: {nota/cont}')
