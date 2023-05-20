"""
Eliezer Silva
Exercício 09
-------------
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

a. Possua uma classe chamada Ponto, com os atributos x e y.
b. Possua uma classe chamada Retangulo, com os atributos largura e altura.
c. Possua uma função para imprimir os valores da classe Ponto
d. Possua uma função para encontrar o centro de um Retângulo.
e. Você deve criar alguns objetos da classe Retangulo.
f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um
objeto da classe Ponto.
g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores
de x e y para o centro do objeto.
h. O valor do centro do objeto deve ser mostrado na tela.
i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def mostrar_retangulo(self):
        return print(f'\nRetângulo\n'
                     f'Largura: {self.largura}\n'
                     f'Altura: {self.altura}')


class Ponto:
    def __init__(self, ponto_x, ponto_y):
        self.ponto_x = ponto_x
        self.ponto_y = ponto_y

    def mostrar_ponto(self):
        return print(f'\nPonto\n'
                     f'Ponto X posição: {self.ponto_x}\n'
                     f'Ponto Y posição: {self.ponto_y}')


def encontrar_centro(retangulo):
    largura = retangulo.largura
    altura = retangulo.altura
    x = f'{largura / 2 :.2f}'
    y = f'{altura / 2 :.2f}'
    print(f'\nPosição centro: x{x}, y{y}')


def encontrar_posicao(retangulo, ponto):
    largura = retangulo.largura
    altura = retangulo.altura
    x = ponto.ponto_x
    y = ponto.ponto_y
    print(f'\nRetângulo\n'
          f'Largura: {largura}, '
          f'Altura: {altura}\n'
          f'Posição ponto: x{x:.2f}, y{y:.2f}')


# estância dos objetos
retangulo1 = Retangulo(6, 8)
retangulo1.mostrar_retangulo()

ponto1 = Ponto(0, 0)
ponto1.mostrar_ponto()

encontrar_centro(retangulo1)

retangulo2 = Retangulo(10, 10)
ponto2 = Ponto(3, 7)
encontrar_posicao(retangulo2, ponto2)
