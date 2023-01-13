"""
Eliezer Silva
Exercício 06
-------------
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o
nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
"""
print()

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

data = input('Insira a data de nascimento [dd/mm/aaaa]: ')
dia = data[0:2:1]
indice_mes = int(data[3:5:1])
mes = meses[indice_mes - 1]
ano = data[6:10:1]

print(f'Você nasceu em {dia} de {mes} de {ano}.')
