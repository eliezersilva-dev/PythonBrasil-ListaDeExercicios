"""
Eliezer Silva
Exercício 14
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""
print()
print('-' * 10 + 'CÁLCULO DE MÉDIA' + '-' * 10)

print()
nota1 = input('Insira a primeira nota [0 à 10]: ')
nota2 = input('Insira a primeira nota [0 à 10]: ')
print()

if not nota1.isnumeric() and not nota2.isnumeric():
    print('Valor digitado INVÁLIDO.')
    quit()
else:
    media = (float(nota1) + float(nota2)) / 2

    if media > 10 or media < 0:
        print('Digite valores entre 0 e 10.')

    elif media <= 10.0 and media >= 9.0:
        print(f'Nota 1: {nota1}\n'
              f'Nota 2: {nota2}\n'
              f'Média: {media}\n'
              f'Conceito A\n'
              f'Aluno(a) APROVADO(A)')
    elif media < 9.0 and media >= 7.5:
        print(f'Nota 1: {nota1}\n'
              f'Nota 2: {nota2}\n'
              f'Média: {media}\n'
              f'Conceito B\n'
              f'Aluno(a) APROVADO(A)')
    elif media < 7.0 and media >= 6.0:
        print(f'Nota 1: {nota1}\n'
              f'Nota 2: {nota2}\n'
              f'Média: {media}\n'
              f'Conceito C\n'
              f'Aluno(a) APROVADO(A)')
    elif media < 6.0 and media >= 4.0:
        print(f'Nota 1: {nota1}\n'
              f'Nota 2: {nota2}\n'
              f'Média: {media}\n'
              f'Conceito D\n'
              f'Aluno(a) REPROVADO(A)')
    elif media < 4.0 and media >= 0.0:
        print(f'Nota 1: {nota1}\n'
              f'Nota 2: {nota2}\n'
              f'Média: {media}\n'
              f'Conceito D\n'
              f'Aluno(a) REPROVADO(A)')
