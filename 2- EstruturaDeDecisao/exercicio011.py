"""
Eliezer Silva
Exercício 11
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o
programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5%.
Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

print()
salario = float(input('Informe o salário: '))
percentual = 0
aumento = 0
novo_salario = 0

if salario <= 280.00:
    percentual = '20%'
    aumento = (salario / 100) * 20
    novo_salario = salario + aumento

elif salario > 280.00 and salario <= 700.00:
    percentual = '15%'
    aumento = (salario / 100) * 15
    novo_salario = salario + aumento

elif salario > 700.00 and salario < 1500.00:
    percentual = '10%'
    aumento = (salario / 100) * 10
    novo_salario = salario + aumento
else:
    percentual = '5%'
    aumento = (salario / 100) * 5
    novo_salario = salario + aumento

print()
print(f'Salário antes do reajuste: R$ {salario:.2f}\n'
      f'Percentual de aumento {percentual}\n'
      f'Valor do aumento salarial R$ {aumento:.2f}\n'
      f'Salário após o reajuste: R$ {novo_salario:.2f}')




