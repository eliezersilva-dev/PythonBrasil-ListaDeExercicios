"""
Eliezer Silva
Exercício 11
-------------
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no
tanque.
b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de
combustível no tanque de gasolina.
d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
e. Forneça um método adicionarGasolina( ), para abastecer o tanque.

Exemplo de uso:
meuFusca = Carro(15);           # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.

"""


# Construindo a classe Carro
class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.tanque = 0

    def adicionar_gasolina(self, litros):
        print('>>> Abastecer...')
        self.tanque += litros
        return print(f'Abastece com {litros} litros de combustível.\n')

    def andar(self, quilometros):
        print('>>> Andar...')
        if self.tanque == 0:
            print('Tanque vazio. Precisa Abastecer.\n')
        elif self.tanque - (quilometros / self.consumo) < 0:
            print('Combustível insuficiente para a viagem.\n')
        else:
            self.tanque = self.tanque - (quilometros / self.consumo)
            print(f'Anda {quilometros} quilômetros\n')

    def obter_gasolina(self):
        print('>>> Nível no tanque...')
        return print(f'Combustível no tanque: {self.tanque} litros.\n')


# Criando um objeto da classe Carro
meu_opala = Carro(1)

# Listando os atributos do objeto
# print(meu_opala.__dict__)
# Listando os métodos do objeto
# for i in meu_opala.__dir__():
#     print(i)

# Testando o objeto
meu_opala.obter_gasolina()
meu_opala.adicionar_gasolina(20)
meu_opala.obter_gasolina()
meu_opala.andar(10)
meu_opala.obter_gasolina()
meu_opala.andar(10)
meu_opala.obter_gasolina()
meu_opala.andar(10)
meu_opala.adicionar_gasolina(20)
meu_opala.andar(30)

#  (•◡•) /
