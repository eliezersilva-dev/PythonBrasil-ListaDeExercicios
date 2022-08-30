"""
Eliezer Lucas
Exercício 08
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês.
"""
nome = input('Digite seu nome: ')
valor_hora = float(input('Informe o valor em reais(R$) da hora trabalhada: '))
qtd_hora = int(input('Informe a quantidade de horas trabalhadas por dia: '))
qtd_dia = int(input('Informe a quantidade de dias trabalhados no mês: '))
salario = (qtd_hora * valor_hora) * qtd_dia
print(f'Prezado {nome}. Seu salário mensal é de {salario:.2f} reais')
