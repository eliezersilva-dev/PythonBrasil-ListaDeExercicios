"""
Eliezer Silva
Exercício 47
-------------
Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas
pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média com as notas restantes).
As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme
o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""
print()
nome = input('Nome do atleta: ')
cont = 1
notas = []

while cont <= 7:
    valor = float(input('Nota: '))
    notas.append(valor)
    cont += 1

print()
print(f'Atleta: {nome}')

for i in notas:
    print(f'Nota: {i}')

print()
print(f'Resultado final:\n'
      f'Atleta: {nome}\n'
      f'Melhor nota: {max(notas)}\n'
      f'Pior nota: {min(notas)}')
notas.sort()
notas.pop(0)
notas.pop(-1)
media = sum(notas) / 5
print(f'Média: {media:.2f}')
