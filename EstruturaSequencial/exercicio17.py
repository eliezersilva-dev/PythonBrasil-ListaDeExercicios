"""
Eliezer Silva
Exercício 17
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os
valores para cima, isto é, considere latas cheias.
"""

largura = float(input('Digite a largura da área a ser pintada: '))
comprimento = float(input('Digite o comprimento da área a ser pintada: '))
area = float(largura * comprimento)
litros = area / 6

latas = int(litros / 18)
if not latas % 18 == 0.0:
    latas += 1
preco_latas = latas * 80

galoes = litros / 3.6
if galoes % 3.6 != 0:
    galoes += 1
preco_galao = galoes * 25

print(f'Apenas latas de 18 litros: {latas} lata(s) R$ {preco_latas:.2f} .')
print(f'Apenas galões de 3.6 litros: {galoes} galao(oes) R$ {preco_galao:.2f} .')




# mistura_lata = int(litros / 18.0)
# mistura_galao = int((litros - (mistura_lata * 18)) / 3.6)
#
# if litros - (mistura_lata * 18) % 3.6 != 0:
#     mistura_galao += 1
#
# p
#
# print('Mistura: %d latas e %d galoes = %.2f' % (
#     mistura_lata, mistura_galao, ((mistura_lata * 80) + (mistura_galao * 25))))