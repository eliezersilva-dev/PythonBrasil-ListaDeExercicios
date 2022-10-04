"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média
das temperaturas.
"""
print()
print('-' * 10 + ' Departamento Estadual de Meteorologia ' + '-' * 10)
print()

temperaturas = []

quantidade = int(input('Quantidade de temperaturas: '))
quantidade_lista = list(range(1, quantidade+1))

cont = 1
for i in quantidade_lista:
    temperaturas.append(int(input(f'Temperatura {cont}: ')))
    cont += 1

maior = max(temperaturas)
menor = min(temperaturas)
media = sum(temperaturas) / quantidade

print(f'Maior temperatura: {maior}°C\n'
      f'Menor temperatura: {menor}°C\n'
      f'Média das temperaturas: {media}°C')
