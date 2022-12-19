"""
Eliezer Silva
Exercício 10
-------------
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre
2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira
jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu
"Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se
tirar um 7 antes de tirar este Ponto novamente.
"""
import random
import time

print()

contador = 0
pontos_jogador = 0


def placar(pontos):
    global pontos_jogador

    if contador == 1:
        pontos_jogador = pontos
        if pontos_jogador == 7 or pontos_jogador == 11:
            print('Natural!! Você ganhou!!')
            quit()
        elif pontos_jogador == 2 or pontos_jogador == 3 or pontos_jogador == 12:
            print('Craps!! Você perdeu!!')
            quit()
        else:
            print(f'Seu ponto é {pontos_jogador}')
        rodada()
    else:
        print(f'Seu ponto: {pontos_jogador}')
        if pontos_jogador == pontos:
            print('Você tirou seu ponto!! Você ganhou!!')
            quit()
        elif pontos == 7:
            print('Você tirou 7!! Você perdeu :(')
            quit()
        else:
            print('Você não tirou seu ponto. Próxima rodada...')
            rodada()


def jogar_dados():
    print()
    print('Jogando os dados...')
    time.sleep(1.7)
    dado_1 = random.randint(1, 6)
    print(f'Dado 1 = {dado_1}')
    time.sleep(1.7)
    dado_2 = random.randint(1, 6)
    print(f'Dado 2 = {dado_2}')
    time.sleep(1.5)
    pontos = dado_1 + dado_2
    print(f'Pontos da rodada = {pontos}')
    placar(pontos)


def rodada():
    global contador

    if contador == 0:
        print('Vamos começar o jogo!')
    else:
        print(f'Próxima rodada.')

    print()
    jogar = input('Jogar dados? [s/n]: ')

    if jogar == 's':
        pass
    else:
        print('Saindo...')
        time.sleep(1.5)
        quit()

    contador += 1
    jogar_dados()


rodada()
