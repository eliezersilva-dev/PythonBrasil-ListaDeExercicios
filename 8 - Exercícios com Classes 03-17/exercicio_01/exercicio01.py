"""
Eliezer Silva
Exercício 01
-------------
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""


class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self, novacor):
        self.cor = novacor

    def mostrar_cor(self):
        return self.cor


bola_1 = Bola('vermelha', '68cm', 'couro')
bola_2 = Bola('laranjada', '80cm', 'couro')

print(bola_1.cor)
print(bola_2.cor)

print(bola_1.__dict__)
print(bola_2.__dict__)

bola_1.trocar_cor('preta')
print(bola_1.mostrar_cor())
