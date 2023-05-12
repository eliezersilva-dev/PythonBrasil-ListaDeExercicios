"""
Eliezer Silva
Exercício 03
-------------
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher);
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""
print()


class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_lado_a(self, novolado_a):
        self.lado_a = novolado_a

    def mudar_lado_b(self, novolado_b):
        self.lado_b = novolado_b

    def calcular_area(self):
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        return (self.lado_a * 2) + (self.lado_b * 2)


print('-'*10 + 'Calcular Piso' + '-'*10)
print()
print('Para calcular informe:')
ladoa = float(input('Medida lado A: '))
ladob = float(input('Medida lado B: '))

print()

retangulo = Retangulo(ladoa, ladob)
print(f'Valor lado A: {retangulo.lado_a}')
print(f'Valor lado B: {retangulo.lado_b}')

print()

print(f'Total de Área: {retangulo.calcular_area()}m²')
print(f'Rodapé de 10cm - Total do Perímetro: {(retangulo.calcular_perimetro()) * 0.10}m²')
