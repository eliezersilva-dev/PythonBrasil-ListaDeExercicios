"""
Eliezer Silva
Exerício 13
------------
Classe Funcionário:
Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double).
Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário.
Escreva um pequeno programa que teste sua classe.
"""


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def ver_nome(self):
        return self.nome

    def ver_salario(self):
        return self.salario


funcionario_teste = Funcionario('Rose Maria', 10000.00)

print(f'\nFuncionário:\n'
      f'Nome: {funcionario_teste.ver_nome()}\n'
      f'Salário: R$ {funcionario_teste.ver_salario()}')
