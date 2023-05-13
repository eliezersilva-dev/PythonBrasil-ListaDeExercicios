"""
Eliezer Silva
Exercício 04
-------------
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura;
Métodos: Envelhercer, engordar, emagrecer, crescer;

Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a
idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""
print()


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, ano):
        if self.idade < 25:
            self.altura = self.altura + 0.5
        self.idade = self.idade + ano

    def engordar(self, quilo):
        self.peso = self.peso + quilo

    def emagrecer(self, quilo):
        self.peso = self.peso - quilo

    def crescer(self, centimetro):
        self.altura = self.altura + centimetro


pessoa1 = Pessoa('Maria', 8, 25, 1.0)
print(pessoa1.nome)
pessoa1.envelhecer(10)
print(pessoa1.idade)
pessoa1.crescer(0.20)
print(pessoa1.altura)
pessoa1.engordar(10)
print(pessoa1.peso)
pessoa1.emagrecer(5)
print(pessoa1.peso)
