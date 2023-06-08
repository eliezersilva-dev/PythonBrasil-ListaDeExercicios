"""
Eliezer Silva
Exercício 10
-------------
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
i. tipoCombustivel;
ii. valorLitro;
iii. quantidadeCombustivel.

b. Possua no mínimo esses métodos:
i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi
colocada no veículo;
ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago
pelo cliente;
iii. alterarValor( ) – altera o valor do litro do combustível;
iv. alterarCombustivel( ) – altera o tipo do combustível;
v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""


# Construindo a classe Bomba de Combustível
class BombaCombustivel:
    def __init__(self, tipo, valor_litro, quantidade):
        self.tipo = tipo
        self.valor_litro = valor_litro
        self.quantidade = quantidade

    def abastecer_valor(self, valor):
        litros = valor / self.valor_litro
        if self.quantidade <= 0:
            print(f'Acabou o Combustível.')
            return operacao_bomba(self)
        elif litros > self.quantidade:
            print(f'Quantidade em estoque insuficiente.\n')

            return operacao_bomba(self)
        else:
            print(f'Abastecido {litros} litros de Combustível.\n')
            self.quantidade = self.quantidade - litros
            print(f'Litros restantes: {self.quantidade}\n')
            return operacao_bomba(self)

    def abastecer_litro(self, litro):
        if self.quantidade <= 0:
            print(f'Acabou o Combustível.')
            return operacao_bomba(self)
        elif litro > self.quantidade:
            print(f'Quantidade em estoque insuficiente.')

            return operacao_bomba(self)
        else:
            self.quantidade = self.quantidade - litro
            valor_pago = litro * self.valor_litro
            print(f'\nQuatidade de Combustível Abastecido: {litro} litros\n'
                  f'Valor Pago: R$ {valor_pago}\n'
                  f'Quantidade restante na Bomba: {self.quantidade} litros\n')
            return operacao_bomba(self)

    def alterar_valor(self, valor):
        self.valor = valor
        return print(f'\nValor do Combustível: R$ {self.valor}\n')

    def alterar_combustivel(self, combustivel):
        self.tipo = combustivel
        return print(f'\nCombustível na Bomba: {self.tipo} litros')

    def alterar_quantidade(self, novo_valor):
        self.quantidade = novo_valor
        return print(f'\nNovo Estoque de {self.tipo} na bomba: {self.quantidade} litros')


# Criando objetos
print('\nConfigure as Bombas de Combustível:\n')

print('Bomba Diesel')
preco = float(input('Valor do Diesel: R$ '))
estoque = float(input('Estoque do Diesel (litros): '))
bomba_diesel = BombaCombustivel('Diesel', preco, estoque)

print()

print('Bomba Gasolina')
preco = float(input('Valor da Gasolina: R$ '))
estoque = float(input('Estoque da Gasolina (litros): '))
bomba_gasolina = BombaCombustivel('Gasolina', preco, estoque)

print()

print('Bomba Etanol')
preco = float(input('Valor de Etanol: R$ '))
estoque = float(input('Estoque de Etanol (litros): '))
bomba_etanol = BombaCombustivel('Etanol', preco, estoque)

print()


# Usando os objetos
def operacao_bomba(bomba):
    print(f'\n----- Bomba {bomba.tipo} -----\n'
          f'Preço (litro): R$ {bomba.valor_litro}\n'
          f'Estoque: {bomba.quantidade} litros\n')

    operacao = input(f'Abastecer litros {" "*len(bomba.tipo)} [1]\n'
                     f'Abastecer R$     {" "*len(bomba.tipo)} [2]\n'
                     f'Alterar Preço do {bomba.tipo} [3]\n'
                     f'Aterar Estoque   {" "*len(bomba.tipo)} [4]\n'
                     f'Trocar de Bomba  {" "*len(bomba.tipo)} [5]\n'
                     f'Opção: ')

    if operacao == '1':
        print('>>> Abastecer Litros:\n')
        litros = float(input('Quantidade (litros): '))
        bomba.abastecer_litro(litros)
    elif operacao == '2':
        print('>>> Abastecer Valor R$:\n')
        valor_pago = float(input('Valor R$: '))
        bomba.abastecer_valor(valor_pago)
    elif operacao == '3':
        print(f'>>> Alterar Preço do {bomba.tipo}\n')
        novo_preco = float(input('Novo valor: R$ '))
        bomba.valor_litro = novo_preco
        print(f'Preço atual do {bomba.tipo}: R$ {bomba.valor_litro}\n')
        operacao_bomba(bomba)
    elif operacao == '4':
        print(f'>>> Alterar estoque de {bomba.tipo}:\n')
        novo_estoque = float(input('Novo estoque (litros): '))
        bomba.quantidade = novo_estoque
        print(f'Estoque atual de {bomba.tipo}: {bomba.quantidade} litros \n')
        operacao_bomba(bomba)
    elif operacao == '5':
        controle_bomba()


def controle_bomba():
    bomba = input('\n----- Controle de Bomba -----\n'
                  '        Diesel   [1]\n'
                  '        Gasolina [2]\n'
                  '        Etanol   [3]\n'
                  '        Sair     [4]\n'
                  'Opção: ')

    if bomba == '1':
        bomba = bomba_diesel
    elif bomba == '2':
        bomba = bomba_gasolina
    elif bomba == '3':
        bomba = bomba_etanol
    elif bomba == '4':
        print('Fechando a Bomba de Combustível...')
        quit()
    else:
        print('Digite uma opção válida.\n')
        controle_bomba()


    operacao_bomba(bomba)


controle_bomba()
