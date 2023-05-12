"""
Eliezer Silva
Exercício 02
-------------
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área
"""


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, novolado):
        self.lado = novolado

    def retornar_valor_lado(self):
        return self.lado

    def calcular_area(self):
        return self.lado * self.lado


quadrado_1 = Quadrado(10)

print(quadrado_1.retornar_valor_lado())
print(quadrado_1.calcular_area())
quadrado_1.mudar_lado(20)
print(quadrado_1.retornar_valor_lado())
print(quadrado_1.calcular_area())
