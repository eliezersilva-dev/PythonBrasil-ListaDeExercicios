"""
Eliezer Silva
Exercício 05
-------------
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.

A classe deve possuir os seguintes atributos:
- número da conta, nome do correntista e saldo.

Os métodos são os seguintes:
- alterarNome, depósito e saque;

No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""
print()


class ContaCorrente:
    def __init__(self, numconta, nome, saldo):
        self.numconta = numconta
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo < valor:
            print('Saldo Insuficiente.')
        else:
            self.saldo = self.saldo - valor


conta1 = ContaCorrente(404, 'Rose', 1000)
print(conta1.__dict__)

print(f'Nome: {conta1.nome} - Saldo: {conta1.saldo}')
conta1.deposito(50)
print(f'Nome: {conta1.nome} - Saldo: {conta1.saldo}')
conta1.saque(2000)
print(f'Nome: {conta1.nome} - Saldo: {conta1.saldo}')
