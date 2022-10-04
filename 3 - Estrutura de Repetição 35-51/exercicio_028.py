"""
Eliezer Lucas
Exercício 28
-------------
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de
CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs
e o valor para em cada um.
"""

print()
quantidade_cd = 3
preco_total = 0
cont = 0

for i in range(quantidade_cd):
    preco_total += float(input(f'Valor do CD {cont+1}: R$ '))
    cont += 1

media = preco_total / quantidade_cd
media = f'{media:.2f}'
media = str(media)
media = media.replace('.', ',')
preco_total_str = f'{preco_total:.2f}'
preco_total_str = str(preco_total_str)
preco_total_str = preco_total_str.replace('.', ',')
print()
print(f'O valor total gasto na coleção foi de R$ {preco_total_str}\n'
      f'Sendo o preço médio de cada CD de R$ {media}')
