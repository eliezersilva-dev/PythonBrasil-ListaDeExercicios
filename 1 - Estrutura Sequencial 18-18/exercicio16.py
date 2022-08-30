"""
Eliezer Silva
Exercício 16
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

largura = float(input('Informe em metros a largura da superfície a ser pintada: '))
comprimento = float(input('Informe em metros o comprimento da superfície a ser pintada: '))
area = largura * comprimento
qtd_litros = round(area / 3)
latas = round(qtd_litros / 18)

if latas % 18 == 0:
    latas = latas + 1

print(f'A área total informada é {area} metros quadrados.\n'
      f'Será necessário {latas} lata(s) de tinta.\n'
      f'O total será R$ {latas * 18:.2f}')
