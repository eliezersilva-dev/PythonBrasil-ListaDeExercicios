"""
Eliezer Silva
Exercício 27
-------------
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

# Cabeçalho
print()
print('-' * 10 + ' Fruteira ' + '-' * 10)
print()

# Tratando entrada
fruta = input('Escolha a fruta [1] Morango / [2] Maçã: ')

if fruta != '1' and fruta != '2':
    print('Digite um valor válido.\n'
          '[1] Morango / [2] Maçã')
    quit()

try:
    quantidade_kg = float(input('Digite a quantidade [Kg]: '))
    if quantidade_kg < 1:
        print('Digite uma quantidade maior que zero.')
        quit()
except ValueError:
    print('Digite uma quantidade válida.')
    quit()

# Variáveis acessórias
preco_morango_abaixo = 2.50
preco_morango_acima = 2.20
preco_maca_abaixo = 1.80
preco_maca_acima = 1.50
valor = 0

# Tratando os dados
if fruta == '1':
    if quantidade_kg <= 5:
        valor = quantidade_kg * preco_morango_abaixo
    elif quantidade_kg > 5:
        valor = quantidade_kg * preco_morango_acima
if fruta == '2':
    if quantidade_kg <= 5:
        valor = quantidade_kg * preco_maca_abaixo
    elif quantidade_kg > 5:
        valor = quantidade_kg * preco_maca_acima

if quantidade_kg > 8 or valor > 25:
    valor = valor - ((valor / 100) * 10)

# Tratando saída
valor = f'{valor:.2f}'
valor = str(valor.replace('.', ','))
print(f'Valor total: R$ {valor}')
