"""
Eliezer Silva
Exercício 12
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7 * altura) - 58
"""

altura = float(input('Digite a altura de uma pessoa: '))
print(f'O peso ideal considerando a altura informada é: {(72.7 * altura - 58):.2f}')
