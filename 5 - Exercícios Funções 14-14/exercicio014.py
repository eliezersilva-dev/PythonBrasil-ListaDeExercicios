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


# Não terminei ainda :(
import itertools
from itertools import combinations, permutations


# def valida_tabela(tabela): # Verifica se a tabela é válida
#     if sum(tabela[:3]) == sum(tabela[3:6]) == sum(tabela[6:10]):
#         if sum(tabela[::3]) == sum(tabela[1::3]) == sum(tabela[2::3]):
#             if sum(tabela[::4]) == sum(tabela[2:8:2]):
#                 print(tabela, ' valida ')
#                 return 1
#            else: return 0
#        else: return 0
#    else:
#        return 0
#
#
# def gera(tab): #gerar as matrizes possíveis
#     cont = 0
#     validos = 0
#     for i in permutations(tab,9):
#         cont += 1
#         validos += validaTabela(i)
#    print(f'total de verificações {cont} e matriz válidas {validos}')
#
# tabela = [1,2,3,4,5,6,7,8,9]
#
# gera(tabela)



for i in itertools.count():
    print(i)