"""
Eliezer Silva
Exercício 08
-------------
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos
comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos,
alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.
Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""


class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = ''

    def comer(self, alimento):
        self.bucho = alimento
        print(f'{self.nome} está comendo {alimento}.')

    def ver_bucho(self):
        print(f'{self.nome} está com o bucho cheio de {self.bucho}.')

    def digerir(self):
        print(f'{self.nome} está digerindo {self.bucho}.')


macaco1 = Macaco('Donkey')
macaco2 = Macaco('kong')

macaco1.comer('banana')
macaco1.ver_bucho()
macaco1.digerir()

macaco2.comer(macaco1.nome)
macaco2.ver_bucho()
macaco2.digerir()

print()
print('Os macacos no Python podem ser canibais :O')
