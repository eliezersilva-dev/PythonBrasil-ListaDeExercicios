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

# Exercício não finalizado. Não encontrei solução em Estrutura Sequencial que atendesse as necessidades do problema;
# Segue solução proposta, no entanto há várias falhas;
# Se você encontrar outra solução, por favor deixe um pull request. Muito Obrigado! Eliezer Silva.

largura = float(input('Digite a largura da área a ser pintada: '))
comprimento = float(input('Digite o comprimento da área a ser pintada: '))
area = float(largura * comprimento)
print(f'A área a ser pintada é de {area} m²')
litros = round(area / 6) * 1.1

latas = round(litros / 18)
if latas % 18 == 0:
    latas += 1
preco_latas = latas * 80

galoes = round(litros / 3.6)
if galoes % 3.6 == 0:
    galoes += 1
preco_galao = galoes * 25

mistura_latas = round(litros / 18)
mistura_galao = round((litros - latas * 18) / 3.6)

if litros - (mistura_latas * 18) % 3.6 == 0:
    mistura_galao += 1

preco_mistura = (mistura_latas * 80) + (mistura_galao * 25)

print('Quantidade a ser usada:')
print(f'Apenas latas de 18 litros: {latas} lata(s) R$ {preco_latas:.2f} .')
print(f'Apenas galões de 3.6 litros: {galoes} galao(oes) R$ {preco_galao:.2f} .')
print(f'Misturando latas e galões: {latas} lata(s) {mistura_galao} galão(ões) R$ {preco_mistura:.2f}')

