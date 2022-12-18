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


def jogar_dados():
    print()
    print('Jogando os dados...')
    time.sleep(3)
    dado_1 = random.randint(1, 6)
    print(f'Dado 1 = {dado_1}')
    time.sleep(3)
    dado_2 = random.randint(1, 6)
    print(f'Dado 2 = {dado_2}')
    time.sleep(1.5)
    pontos = dado_1 + dado_2
    print(f'Pontos = {pontos}')
    

jogar_dados()


