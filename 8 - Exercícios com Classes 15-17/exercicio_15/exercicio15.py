"""
Eliezer Silva
Exercício 15
-------------
Classe Bichinho Virtual++:
Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e
por quanto tempo ele brinca com o bichinho.
Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
"""
import time


class Bichinho:
    def __init__(self, nome, nascimento):
        self.nascimento = nascimento
        self.nome = nome
        self.valor_idade = 0
        self.idade = 'Bebê'
        self.valor_saude = 5
        self.saude = 'Saudável'
        self.valor_fome = 2
        self.fome = 'Faminto'
        self.valor_humor = 5
        self.humor = 'Feliz'

    def alterar_idade(self):
        agora = time.time()
        self.valor_idade = float(f'{(self.nascimento - agora) * (-1):.2f}')

    def alterar_saude(self):
        self.valor_saude -= self.valor_idade * 0.01
        self.valor_humor -= self.valor_idade * 0.01
        self.valor_fome -= 0.3

        if self.valor_fome < 5:
            self.valor_saude -= 0.02
        else:
            self.valor_saude += 0.5

        if self.valor_humor < 5:
            self.valor_saude -= 0.02
        else:
            self.valor_saude += 0.5

    def alterar_fome(self, comida):
        self.valor_fome += comida
        menu(self)

    def alterar_humor(self, valor):
        self.valor_humor += valor

        if self.valor_fome < 5:
            self.valor_humor -= 0.5
        elif self.valor_fome > 5:
            self.valor_humor += 0.5

        self.alterar_fome(0)

    def retornar_idade(self):
        if self.valor_idade <= 15:
            self.idade = 'Bebê'
        elif self.valor_idade <= 30:
            self.idade = 'Criança'
        elif self.valor_idade <= 45:
            self.idade = 'Adolescente'
        elif self.valor_idade <= 60:
            self.idade = 'Adulto'
        elif self.valor_idade <= 75:
            self.idade = 'Idoso'
        elif self.valor_idade <= 150:
            print(f'{self.nome} está velhinho...\n')
        else:
            time.sleep(1.2)
            print(f'{self.nome} faleceu...\n'
                  f':´(')
            quit()
        return print(f'{self.nome} é um {self.idade}')

    def retornar_saude(self):
        if self.valor_saude < -10:
            print(f'{self.nome} ficou muito doente e morreu...')
            quit()
        elif self.valor_saude <= 2:
            self.saude = 'Muito Doente'
        elif 2 < self.valor_saude < 5:
            self.saude = 'Doente'
        elif 5 <= self.valor_saude < 8:
            self.saude = 'Saudável'
        else:
            self.saude = 'Muito Saudável'
        return print(f'Saúde: {self.nome} está {self.saude}')

    def retornar_fome(self):
        if self.valor_fome < -10:
            print(f'{self.nome} morreu de fome...\n'
                  f'RIP...')
            quit()
        elif 0 <= self.valor_fome <= 2:
            self.fome = 'Muito Faminto'
        elif 2 < self.valor_fome < 5:
            self.fome = 'Faminto'
        elif 5 <= self.valor_fome < 7:
            self.fome = 'Satisfeito'
        elif 7 <= self.valor_fome < 8:
            self.fome = 'Cheio'
        elif 8 <= self.valor_fome <= 10:
            self.fome = 'Muito Cheio'
        elif self.valor_fome > 13:
            print(f'{self.nome} explodiu de tanto comer...\n'
                  f'RIP...')
            quit()
        return print(f'Fome: {self.nome} está {self.fome}')

    def retornar_humor(self):
        if self.valor_humor < 2:
            self.humor = 'Muito Triste'
        elif 2 <= self.valor_humor < 5:
            self.humor = 'Triste'
        elif 5 <= self.valor_humor < 7:
            self.humor = 'Feliz'
        elif 7 <= self.valor_humor < 8:
            self.humor = 'Muito Feliz'
        elif self.valor_humor >= 8:
            self.humor = 'Hiper Feliz'
        return print(f'Humor: {self.nome} está {self.humor}')


def menu(bichinho):
    bichinho.retornar_idade()
    bichinho.retornar_saude()
    bichinho.retornar_fome()
    bichinho.retornar_humor()

    print()

    bichinho.alterar_idade()
    bichinho.alterar_saude()

    print('-' * 6 + ' MENU ' + 6 * '-')
    opcao = input('Alimentar      [1]\n'
                  'Brincar        [2]\n'
                  'Não fazer nada [3]\n'
                  'Sair           [0]\n'
                  '>>> Opção: ')

    if opcao == '1':
        print(f'{bichinho.nome} está comendo...\n')
        time.sleep(1)
        bichinho.alterar_fome(1)
    elif opcao == '2':
        print(f'{bichinho.nome} está brincando...\n')
        time.sleep(1)
        bichinho.alterar_humor(1)
    elif opcao == '3':
        print(f'{bichinho.nome} não está fazendo nada...\n')
        time.sleep(1)
        bichinho.alterar_humor(-0.2)
    elif opcao == '0':
        print(f'{bichinho.nome} está dizendo adeus...\n')
        time.sleep(1)
        print('Obrigado por cuidar de mim!!\n'
              'Adeus :)')
        quit()
    else:
        menu(bichinho)


def criar_bichinho():
    print('\nCrie seu Bichinho Virtual')
    nome = input('>>> Dê um nome para o seu bichinho: ')
    nascimento = time.time()
    bichinho = Bichinho(nome, nascimento)
    print('Seu Bichinho nasceu...\n')
    time.sleep(1.2)
    menu(bichinho)


criar_bichinho()
