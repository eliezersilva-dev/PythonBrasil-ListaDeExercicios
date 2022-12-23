"""
Eliezer Silva
Exercício 007
-------------
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a
função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro
valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total
de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso,
cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 1% de juros por dia de atraso.
"""

print()

relatorio_diario = []


def relatorio():
    print()
    print(f'Relatório Diário\n'
          f'Total de prestações pagas no dia: {len(relatorio_diario)}\n'
          f'Valor das prestações pagas: {sum(relatorio_diario)}')
    quit()


def valor_pagamento(valor, dias):
    prestacao = 0

    if dias == 0:
        prestacao = valor
        relatorio_diario.append(prestacao)
        print(f'Valor total da prestação: R$ {prestacao}')
        print()
    else:
        prestacao_acrescimo = valor + ((valor * 3) / 100)
        multa = ((valor * 3) / 100) * dias
        prestacao = prestacao_acrescimo + multa
        relatorio_diario.append(prestacao)
        print(f'Valor total da prestação: R$ {prestacao}')
        print()


    inserir_pagamentos()


def inserir_pagamentos():
    valor = float(input('Valor prestação [0 para finalizar]: R$ '))

    if valor == 0:
        relatorio()

    dias = float(input('Dias de atraso: '))
    valor_pagamento(valor, dias)


inserir_pagamentos()
