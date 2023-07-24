"""
Eliezer Silva
Exercício 07
-------------
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade
Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade

Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma
combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para
armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""


class Bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 100
        self.saude = 100
        self.idade = 0

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        print(f'O novo nome do bichinho é: {self.nome}')

    def alterar_fome(self, valor):
        self.fome += valor
        print(f'{self.nome} está com a fome no valor de: {self.fome}')

    def alterar_saude(self, valor):
        self.saude += valor
        print(f'{self.nome} está com a saúde no valor de: {self.saude}')

    def alterar_idade(self, valor):
        self.idade += valor
        print(f'{self.nome} está com a idade no valor de: {self.idade}')

    def retornar_nome(self):
        return print(f'O nome do bichinho é: {self.nome}')

    def retornar_fome(self):
        return print(f'A fome de {self.nome} está no valor de: {self.fome}')

    def retornar_saude(self):
        return print(f'A saude de {self.nome} está no valor de: {self.saude}')

    def retornar_idade(self):
        return print(f'A idade de {self.nome} está no valor de: {self.idade}')

    def humor(self):
        valor_humor = self.fome + self.saude
        if valor_humor >= 50:
            print(f'{self.nome} está feliz :)')
        else:
            print(f'{self.nome} está triste :(')


# Execução do script
bichinho = Bichinho('Bob')
print(bichinho.__dict__)
bichinho.retornar_nome()
bichinho.alterar_fome(10)
bichinho.alterar_saude(10)
bichinho.retornar_fome()
bichinho.humor()
