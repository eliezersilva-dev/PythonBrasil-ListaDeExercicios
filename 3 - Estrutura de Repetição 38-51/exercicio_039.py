"""
Eliezer Silva
Exercício 39
-------------
Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno
mais alto e o mais baixo. Mostre o número do aluno mais alto
e o número do aluno mais baixo, junto com suas alturas.
"""
print()

alunos = {}
cont = 1

while cont < 11:
    # alunos[f'Aluno{cont}'] = input(f'Digite a altura do Aluno {cont}: ') outra forma de inserir valores no dicionário
    alunos.update({f'aluno {cont}': int(input(f'Digite a altura do Aluno {cont} em centímetros: '))})
    cont += 1

print(alunos)
print(f'Aluno mais alto: {max(alunos, key= alunos.get)} com {max(alunos.values())} cm')  # imprimi maior key e maior value
print(f'Aluno mais baixo: {min(alunos, key=alunos.get)} com {min(alunos.values())} cm')  # imprimi menor key e menor value
print(f'A média da altura dos alunos é de {sum(alunos.values()) / len(alunos)}cm')  # soma values divide pelo len
