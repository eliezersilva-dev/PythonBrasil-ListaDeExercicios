"""
Eliezer Silva
Exercício 14
-------------
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a
soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4
1  5  9
6  7  2

Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
"""
from itertools import permutations
print()


def valida_tabela(tabela):
    if sum(tabela[:3]) == sum(tabela[3:6]) == sum(tabela[6:10]):
        if sum(tabela[::3]) == sum(tabela[1::3]) == sum(tabela[2::3]):
            if sum(tabela[::4]) == sum(tabela[2:8:2]):
                print('Quadrado válido:')
                print(f'{tabela[:3]}\n'
                      f'{tabela[3:6]}\n'
                      f'{tabela[6:10]}')
                print()


def gera_tabela(tabela):
    for i in permutations(tabela, 9):
        valida_tabela(i)


tabela = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gera_tabela(tabela)
