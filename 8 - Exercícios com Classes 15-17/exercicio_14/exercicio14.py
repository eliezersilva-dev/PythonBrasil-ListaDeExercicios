"""
Eliezer Silva
Exercício 14
-------------
Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o
salário do funcionário em uma certa porcentagem.
Exemplo de uso:

harry=funcionário("Harry",25000)
harry.aumentarSalario(10)
"""


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def ver_nome(self):
        return self.nome

    def ver_salario(self):
        return self.salario

    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)



funcionario_teste = Funcionario('Rose Maria', 10000)

print(f'\nFuncionário:\n'
      f'Nome: {funcionario_teste.ver_nome()}\n'
      f'Salário: R$ {funcionario_teste.ver_salario()}')

funcionario_teste.aumentar_salario(20)

print(f'\nFuncionário:\n'
      f'Nome: {funcionario_teste.ver_nome()}\n'
      f'Salário: R$ {funcionario_teste.ver_salario()}')
