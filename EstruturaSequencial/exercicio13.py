"""
Eliezer Silva
Exercício 13
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as
seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
altura = float(input('Digite o peso de uma pessoa: '))
print(f'Para uma mulher com a altura {altura} o peso ideal seria {(62.1 * altura) - 44.7:.2f}')
print(f'Para um homem com a altura {altura} o peso ideal seria {(72.7 * altura) - 58:.2f}')
