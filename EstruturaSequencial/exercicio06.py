"""
Eliezer Silva
Exercício 06
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
raio = float(input('Informe o raio de um círculo: '))
area = float((raio ** 2) * 3.14)  # (A = π r²) pi=3,1415
print(f'Com um círculo de raio {raio} temos um círculo de área {area}.')
