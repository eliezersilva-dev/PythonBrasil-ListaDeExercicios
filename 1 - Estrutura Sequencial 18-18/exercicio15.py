"""
Eliezer Silva
Exercício 15
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
* salário bruto.
* quanto pagou IR
* quanto pagou ao INSS.
* quanto pagou ao sindicato.
* o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
# input dos valores
valor_hora = float(input('Informe o valor da hora trabalhada: '))
qta_hora_dia = float(input('Informa a quantidade de horas trabalhadas por dia: '))
qta_dia_mes = float(input('Informe a quantidade de dias trabalhados no mês: '))
# cálculo do salário bruto
salario_bruto = qta_hora_dia * valor_hora * qta_dia_mes
# cálculo dos descontos
desconto_ir = (salario_bruto / 100) * 11
desconto_inss = (salario_bruto / 100) * 8
desconto_sindicato = (salario_bruto / 100) * 5
total_desconto = desconto_ir + desconto_inss + desconto_sindicato
# cáculo do salário liquido
salario_liquido = salario_bruto - total_desconto
# print dos resultados
print(f'O salário bruto mensal é de R$ {salario_bruto:.2f}\n'
      f'Descontos: \n' 
      f'IR: R$ {desconto_ir:.2f}\n'
      f'INSS: R$ {desconto_inss:.2f}\n'
      f'Sindicato: R$ {desconto_sindicato:.2f}\n'
      f'Total a receber: R$ {salario_liquido:.2f}')
