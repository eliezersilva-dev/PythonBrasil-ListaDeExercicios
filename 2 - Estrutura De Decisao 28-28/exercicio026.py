"""
Eliezer Silva
Exercício 26
-------------

Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
- até 20 litros, desconto de 3% por litro;
- acima de 20 litros, desconto de 5% por litro.
Gasolina:
- até 20 litros, desconto de 4% por litro;
- acima de 20 litros, desconto de 6% por litro.
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro
da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

# Cabeçalho
print()
print('-' * 10 + ' Posto de Gasolina ' + '-' * 10)
print()

# Tratando entrada combustível
combustivel = input('Escolha o combustível [G-gasolina / A-alcool]: ')
combustivel = combustivel.upper()

print()

if combustivel != 'G' and combustivel != 'A':
    print('Escolha G-gasolina ou A-álcool.')
    quit()

# Tratando entrada quantidade
quantidade = 0

try:
    quantidade = float(input('Digite a quantidade de litros: '))
except ValueError:
    print('Erro - Digite uma quantidade válida.\n'
          'Use apenas números.\n'
          'Use ponto(.) ao invés de vírgula(,).')
    quit()

if quantidade <= 0:
    print('Digite uma quantidade igual ou maior que 1(um).')
    quit()

print()

# Variáveis acessórias
preco_a = 1.90
preco_g = 2.50
preco = 0
desconto = 0
preco_final = 0

# Processando os dados
if combustivel == 'A':
    if quantidade <= 20:
        preco = quantidade * preco_a
        desconto = (preco / 100) * 3
        preco_final = preco - desconto
    if quantidade > 20:
        preco = quantidade * preco_a
        desconto = (preco / 100) * 5
        preco_final = preco - desconto

if combustivel == 'G':
    if quantidade <= 20:
        preco = quantidade * preco_g
        desconto = (preco / 100) * 4
        preco_final = preco - desconto
    if quantidade > 20:
        preco = quantidade * preco_g
        desconto = (preco / 100) * 6
        preco_final = preco - desconto

# Tratando saída final
if combustivel == 'G':
    combustivel = 'Gasolina'
if combustivel == 'A':
    combustivel = 'Álcool'

preco = f'{preco:.2f}'
preco = str(preco)
preco = preco.replace('.', ',')

desconto = f'{desconto:.2f}'
desconto = str(desconto)
desconto = desconto.replace('.', ',')

preco_final = f'{preco_final:.2f}'
preco_final = str(preco_final)
preco_final = preco_final.replace('.', ',')

# Saída final
print(f'{quantidade:.2f} litros de {combustivel}.\n'
      f'Valor: R$ {preco}\n'
      f'Desconto: R$ {desconto}\n'
      f'Valor total a pagar: R$ {preco_final}')
