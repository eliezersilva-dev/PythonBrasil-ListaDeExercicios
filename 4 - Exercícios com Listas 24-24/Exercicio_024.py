"""
Eliezer Silva
Exercício 24
-------------
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor.
Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para
gerar numeros aleatórios, simulando os lançamentos dos dados.
"""
import random

print()

jogadas = []
valores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}


def resultado():
    for k, v in valores.items():
        for i in jogadas:
            if i == k:
                valores[k] += 1
    for chave, valor in valores.items():
        print(f'Lado {chave}: {valor} vezes.')


def lancar_dados():
    for i in range(100):
        jogadas.append(random.randint(1, 6))
    resultado()


lancar_dados()
# :)
