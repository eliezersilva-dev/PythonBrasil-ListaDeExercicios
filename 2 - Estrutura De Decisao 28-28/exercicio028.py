"""
Eliezer Silva
Exercício 28
------------

O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar APENAS UM dos tipos de carne
da promoção, porém não há limites para a quantidade de carne por cliente. Se a compra for
feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um
cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
tipo de pagamento, valor do desconto e valor a pagar.
"""

print()
print('-' * 10 + ' Fruteira ' + '-' * 10)
print()

produto = input('Escolha um produto:\n'
                '[1] Filé Duplo\n'
                '[2] Alcatra\n'
                '[3] Picanha\n'
                '-> ')
print()

if produto != '1' and produto != '2' and produto != '3':
    print('Digite um valor válido')
    quit()

quantidade = float(input('Digite a quantidade desejada [Kg]: '))
print()
if quantidade < 1:
    print('Digite uma quantidade maior que zero.')

forma_pagamento = input('Escolha a forma de pagamento:\n'
                        '[1] Cartão de crédito\n'
                        '[2] Outros\n'
                        '-> ')
print()

if forma_pagamento != '1' and forma_pagamento != '2':
    print('Escolha uma forma de pagamento válida.')
    quit()

preco = 0
desconto = 0
valor_total = 0

file_abaixo = 4.90
file_acima = 5.80

alcatra_abaixo = 5.90
alcatra_acima = 6.80

picanha_abaixo = 6.90
picanha_acima = 7.80


if produto == '1':
    produto = 'Filé duplo'
    if quantidade <= 5:
        preco = quantidade * file_abaixo
    if quantidade > 5:
        preco = quantidade * file_acima

if produto == '2':
    produto = 'Alcatra'
    if quantidade <= 5:
        preco = quantidade * alcatra_abaixo
    if quantidade > 5:
        preco = quantidade * alcatra_acima

if produto == '3':
    produto = 'Picanha'
    if quantidade <= 5:
        preco = quantidade * picanha_abaixo
    if quantidade > 5:
        preco = quantidade * picanha_acima

if forma_pagamento == '1':
    forma_pagamento = 'Cartão de crédito.'
    desconto = (preco * 5) / 100
    valor_total = preco - desconto
if forma_pagamento == '2':
    forma_pagamento = 'Outros'
    desconto = '(sem desconto)'
    valor_total = preco

print(f'Cupom fiscal:\n'
      f'Produto: {produto}\n'
      f'Quantidade: {quantidade} Kg\n'
      f'Preço total: R$ {preco:.2f}\n'
      f'Forma de pagamento: {forma_pagamento}\n'
      f'Desconto: R$ {desconto}\n'
      f'Valor total a pagar: R$ {valor_total:.2f}')







