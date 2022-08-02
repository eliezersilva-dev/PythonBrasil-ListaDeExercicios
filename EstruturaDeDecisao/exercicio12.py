"""
Eliezer Silva
Exercício 12
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende
do salário bruto (conforme tabela abaixo), INSS 10 % e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos
os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        (-) Sindicato (3%)              : R$   33,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  198,00
        Salário Liquido                 : R$  902,00
"""
print()
print('************ CÁLCULO SALÁRIO ************')
print()

valor_hora = float(input('Informe o valor da hora: R$ '))
quantidade_horas = float(input('Informe a quantidade de horas trabalhadas no mês: '))
print()

salario_bruto = valor_hora * quantidade_horas
imposto_renda = 0
inss = 0
fgts = 0
sindicato = 0
total_desconto = 0
salario_liquido = 0

if salario_bruto <= 900:
    imposto_renda = 'Isento'
    inss = (salario_bruto / 100) * 10
    fgts = (salario_bruto / 100) * 11
    sindicato = (salario_bruto / 100) * 3
    total_desconto = inss + sindicato
    salario_liquido = salario_bruto - total_desconto
    print(f'Salário bruto: {quantidade_horas} horas x R$ {valor_hora:.2f}: R$ {salario_bruto:.2f}\n'
          f'(-) IR:             ISENTO\n'
          f'(-) INSS (10%):     R$: {inss:.2f}\n'
          f'(-) SINDICATO (3%): R$: {sindicato:.2f}\n'
          f'FGTS (11%) -        Valor pago pela empresa.\n'
          f'Total de descontos: R$ {total_desconto:.2f}\n'
          f'Salário Liquido:    R$ {salario_liquido:.2f}\n')

elif salario_bruto <= 1500:
    imposto_renda = (salario_bruto / 100) * 5
    inss = (salario_bruto / 100) * 10
    fgts = (salario_bruto / 100) * 11
    sindicato = (salario_bruto / 100) * 3
    total_desconto = inss + sindicato + imposto_renda
    salario_liquido = salario_bruto - total_desconto
    print(f'Salário bruto: {quantidade_horas} horas x R$ {valor_hora:.2f}: R$ {salario_bruto:.2f}\n'
          f'(-) IR (5%):        R$: {imposto_renda:.2f}\n'
          f'(-) INSS (10%):     R$: {inss:.2f}\n'
          f'(-) SINDICATO (3%): R$: {sindicato:.2f}\n'
          f'FGTS (11%) -        Valor pago pela empresa.\n'
          f'Total de descontos: R$ {total_desconto:.2f}\n'
          f'Salário Liquido:    R$ {salario_liquido:.2f}\n')

elif salario_bruto <= 2500:
    imposto_renda = (salario_bruto / 100) * 10
    inss = (salario_bruto / 100) * 10
    fgts = (salario_bruto / 100) * 11
    sindicato = (salario_bruto / 100) * 3
    total_desconto = inss + sindicato + imposto_renda
    salario_liquido = salario_bruto - total_desconto
    print(f'Salário bruto: {quantidade_horas} horas x R$ {valor_hora:.2f}: R$ {salario_bruto:.2f}\n'
          f'(-) IR (10%):       R$: {imposto_renda:.2f}\n'
          f'(-) INSS (10%):     R$: {inss:.2f}\n'
          f'(-) SINDICATO (3%): R$: {sindicato:.2f}\n'
          f'FGTS (11%) -        Valor pago pela empresa.\n'
          f'Total de descontos: R$ {total_desconto:.2f}\n'
          f'Salário Liquido:    R$ {salario_liquido:.2f}\n')

else:
    imposto_renda = (salario_bruto / 100) * 20
    inss = (salario_bruto / 100) * 10
    fgts = (salario_bruto / 100) * 11
    sindicato = (salario_bruto / 100) * 3
    total_desconto = salario_bruto - inss - sindicato - imposto_renda
    salario_liquido = salario_bruto - total_desconto
    print(f'Salário bruto: {quantidade_horas} horas x R$ {valor_hora:.2f}: R$ {salario_bruto:.2f}\n'
          f'(-) IR (20%):       R$: {imposto_renda:.2f}\n'
          f'(-) INSS (10%):     R$: {inss:.2f}\n'
          f'(-) SINDICATO (3%): R$: {sindicato:.2f}\n'
          f'FGTS (11%) -        Valor pago pela empresa.\n'
          f'Total de descontos: R$ {total_desconto:.2f}\n'
          f'Salário Liquido:    R$ {salario_liquido:.2f}\n')
