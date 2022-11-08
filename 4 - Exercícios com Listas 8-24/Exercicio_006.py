"""
Eliezer Silva
Exercício 06
-------------
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""

print()
print('-'*10+' MÉDIA '+10*'-')
print()

medias = []
cont_global = 1

while cont_global <= 3:
    cont_local = 1
    aluno = []
    print()
    print(f'Notas Aluno {cont_global}')

    while cont_local <= 4:
        aluno.append(float(input(f'Nota {cont_local}: ')))
        cont_local += 1

    var_media = sum(aluno) / 4
    if var_media >= 7:
        medias.append(f'Aluno {cont_global} média: {var_media}')

    cont_global += 1

print()
print('Aluno(s) com média maior ou igual a 7:')
for i in medias:
    print(i)
