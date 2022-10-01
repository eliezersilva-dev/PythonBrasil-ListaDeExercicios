"""
Eliezer Silva
Exercício 27
------------
Faça um programa que calcule o número médio de alunos por turma. Para isto,
peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
"""

print()

quantidade_turma = int(input('Digite a quantidade de turmas: '))
print()
turma = 0
cont = 0
for i in range(quantidade_turma):
    turma += int(input(f'Digite a quantidade de alunos da turma {cont+1}: '))
    cont += 1
print()
print(f'A média de alunos por turma é de {turma/quantidade_turma:.2f} alunos.')
