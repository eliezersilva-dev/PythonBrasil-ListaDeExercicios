"""
Eliezer Silva
Exercício 41
-------------
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25

Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""

print()
divida = float(input('Valor da dívida: R$ '))
print()
qtd_parcela = 0
juros = 10
valor_juros = 0
valor_parcela = 0
parcelas = [3, 6, 9, 12]

print(f'Valor da Dívida: R$ {divida}\n'
      f'Quantidade de Parcelas: 01\n'
      f'Valor dos Juros: R$ 0,00\n'     
      f'Valor da Parcela: R$ {divida},00\n'
      f'Valor total: R$ {divida + valor_juros:.2f}')
print()


for i in parcelas:
    qtd_parcela = i
    valor_juros = (divida / 100) * juros
    valor_parcela = (divida + valor_juros) / qtd_parcela
    print(f'Valor da Dívida: R$ {divida}\n'
          f'Quantidade de Parcelas: 0{i}\n'
          f'Valor dos Juros: R$ {valor_juros:.2f}\n'          
          f'Valor da Parcela: R$ {valor_parcela:.2f}\n'
          f'Valor total: R$ {divida + valor_juros:.2f}')
    juros += 5
    print()
