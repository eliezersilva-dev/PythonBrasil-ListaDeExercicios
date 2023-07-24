"""
Eliezer Silva
Exercício 12
-------------
Classe Conta de Investimento:
Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um
atributo taxaJuros.
Forneça um construtor que configure tanto o saldo inicial como a taxa de juros.
Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.
Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%.
Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
"""


class ContaInvestimento:
    def __init__(self, saldo, taxa):
        self.saldo = saldo
        self.taxa = taxa

    def adicione_juros(self):
        self.saldo += self.saldo * 0.1
        return self.saldo


conta_poupanca = ContaInvestimento(1000, 10)
print(f'\nSaldo Conta Poupança: R$ {conta_poupanca.saldo}\n')

for i in range(0, 5):
    print(f'Saldo R$ {conta_poupanca.saldo} + 10% juros: R$ {conta_poupanca.adicione_juros()}')
