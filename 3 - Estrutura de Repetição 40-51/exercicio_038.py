"""
Eliezer Silva
Exercício 38
-------------
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo
que o usuário digite o salário inicial do funcionário.
"""

from datetime import datetime

print()

data_atual = datetime.now()
ano_atual = data_atual.year

salario = float(input('Informe o salário do funcionário no ano de 1997: R$ '))
percentual = 1.5
aumento = (salario / 100) * percentual
salario = salario + aumento

for ano in range(1997, ano_atual + 1):
    percentual = percentual * 2
    aumento = (salario / 100) * percentual
    salario += aumento

salario = str(f'{salario:.2f}')
salario = salario.replace('.', ',')
print(f'No ano corrente({ano_atual}) o salário atualizado é de: R$ {salario}')
