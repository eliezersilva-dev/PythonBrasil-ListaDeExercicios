"""
Eliezer Silva
Exercício 04
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
nota_1 = float(input('Digite a primeira nota bimestral: '))
nota_2 = float(input('Digite a segunda nota bimestral: '))
nota_3 = float(input('Digite a terceira nota bimestral: '))
nota_4 = float(input('Digite a quarta nota bimestral: '))
media = float((nota_1 + nota_2 + nota_3 + nota_4) / 4)
print(f'A média das notas informadas é {media:.2f}')
