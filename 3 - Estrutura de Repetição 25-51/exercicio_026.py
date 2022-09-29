"""
Eliezer Silva
Exercício 26
-------------
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
-------------
Obs: Não foram tratados as exceções.
"""

print()
print('-' * 10 + ' Eleição ' + '-' * 10)
print()

print('Escolha entre os candidatos:\n'
      'Candidato1 [1]\n'
      'Candidato2 [2]\n'
      'Candidato3 [3]\n')

candidatos = {'candidato1': 0, 'candidato2': 0, 'candidato3': 0}

eleitores = int(input('Digite a quantidade de eleitores que irão votar: '))
eleitores = list(range(eleitores))
cont = 0

for i in eleitores:
    voto = int(input(f'Eleitor {cont+1}.\n'
                     f'Escolha seu candidato [1/2/3]: '))
    print()

    if voto == 1:
        candidatos['candidato1'] += 1
    if voto == 2:
        candidatos['candidato2'] += 1
    if voto == 3:
        candidatos['candidato3'] += 1

    cont += 1

print(f'O candidato1 obteve {candidatos["candidato1"]} votos')
print(f'O candidato2 obteve {candidatos["candidato2"]} votos')
print(f'O candidato3 obteve {candidatos["candidato3"]} votos')
print()
print(f'O vencedor foi:\n'
      f'{max(candidatos)} com {max(candidatos.values())} votos.')
