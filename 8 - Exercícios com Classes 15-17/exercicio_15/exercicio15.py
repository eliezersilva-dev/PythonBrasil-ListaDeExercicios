"""
Eliezer Silva
Exercício 15
-------------
Classe Bichinho Virtual++:
Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e
por quanto tempo ele brinca com o bichinho.
Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
"""
# Não terminei...ainda :)

import time


class Bichinho:
    def __init__(self, nome, nascimento):
        self.nascimento = nascimento
        self.nome = nome
        self.valor_fome = 0
        self.fome = 'Muito Faminto'
        self.valor_saude = 10
        self.saude = 'Saudável'
        self.valor_idade = 0
        self.idade = 'Bebê'

        self.humor = 'Feliz'

    def alterar_idade(self):
        agora = time.time()
        self.valor_idade = float(f'{(self.nascimento - agora) * (-1):.2f}')
        print(self.valor_idade)
        if self.valor_idade <= 15:
            self.idade = self.idade
        elif self.valor_idade <= 30:
            self.idade = 'Criança'
        elif self.valor_idade <= 45:
            self.idade = 'Adolescente'
        elif self.valor_idade <= 60:
            self.idade = 'Adulto'
        elif self.valor_idade <= 75:
            self.idade = 'Idoso'
        elif self.valor_idade <= 100:
            print(f'{bichinho.nome} está velhinho...\n')
        else:
            time.sleep(1.2)
            print(f'{self.nome} faleceu...\n'
                  f':´(')
            quit()





    def alterar_saude(self):
        print(f'{self.nome} está {self.saude}')

    def alterar_fome(self, valor):
        print(self.valor_fome)
        self.valor_fome += valor
        print(self.valor_fome)
        if self.valor_fome < 0:
            print(f'{self.nome} morreu de fome...\n'
                  f'RIP...')
            quit()
        elif 0 <= self.valor_fome <= 2:
            self.fome = 'Muito Faminto'
            menu(self)
        elif 2 < self.valor_fome < 5:
            self.fome = 'Faminto'
            menu(self)
        elif 5 <= self.valor_fome < 7:
            self.fome = 'Satisfeito'
            menu(self)
        elif 7 <= self.valor_fome < 8:
            self.fome = 'Cheio'
            menu(self)
        elif 8 <= self.valor_fome <= 10:
            self.fome = 'Muito Cheio'
            menu(self)
        else:
            print(f'{self.nome} explodiu de tanto comer...\n'
                  f'RIP...')
            quit()


    def retornar_idade(self):
        return print(f'{self.nome} é um {self.idade}')

    def retornar_saude(self):
        return print(f'Saúde: {self.nome} está {self.saude}')

    def retornar_fome(self):
        return print(f'Fome: {self.nome} está {self.fome}')




    def humor(self):
        return self.humor()






def menu(bichinho):
    bichinho.retornar_idade()
    bichinho.retornar_saude()
    bichinho.retornar_fome()
    # f'{bichinho.nome} está {bichinho.humor()}')


    print()

    bichinho.alterar_idade()

    print('-' * 3 + ' MENU ' + 3 * '-')
    opcao = input('Alimentar [1]\n'
                  'Brincar   [2]\n'
                  'Sair      [0]\n'
                  '>>> Opção: ')

    if opcao == '1':
        print(f'{bichinho.nome} está comendo...\n')
        bichinho.alterar_fome(1)
    elif opcao == '2':
        pass
    elif opcao == '0':
        pass
    else:
        menu(bichinho)


def criar_bichinho():
    print('\nCrie seu Bichinho Virtual')
    nome = input('>>> Dê um nome para o seu bichinho: ')
    nascimento = time.time()
    bichinho = Bichinho(nome, nascimento)
    print('Seu Bichinho nasceu...\n')
    print(bichinho.__dict__)
    time.sleep(1.2)
    menu(bichinho)


criar_bichinho()



