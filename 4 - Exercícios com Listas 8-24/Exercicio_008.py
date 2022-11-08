"""
Eliezer Silva
Exercício 08
-------------
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

print()

pessoas = []
idade = []
altura = []
cont = 1

while cont <= 5:
    print(f'Pessoa {cont}')
    pessoas.append(f'Pessoa {cont}')
    idade.append(input('Idade: '))
    altura.append(input('Altura: '))
    cont += 1
    print()

print(f'Pessoas: {pessoas}')
print(f'Pessos invertidas: {list(reversed(pessoas))}')
print()

print(f'Altura: {altura}')
print(f'Altura invertidas: {list(reversed(altura))}')
print()

print(f'Idades: {idade}')
print(f'Idades invertidas: {list(reversed(idade))}')
print()


# Resolução usando Dicionário (dict)
# dicionario = {
#     'pessoa 1': {'idade': 10, 'altura': 10},
#     'pessoa 2': {'idade': 20, 'altura': 20},
#     'pessoa 3': {'idade': 30, 'altura': 30},
# }
# print(dicionario)
#
# dicionario_reverso = list(reversed(dicionario.items()))
# print(dicionario_reverso)
