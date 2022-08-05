"""
Eliezer Silva
Exercício 05
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

print('#################### MÉDIA ####################')

nota1 = float(input('Digite a primeira nota [valor entre 0 e 10]: '))
nota2 = float(input('Digite a segunda nota [valor entre 0 e 10]: '))

nota2 = float(nota2)
media = (nota1 + nota2) / 2

print(f'Primeira nota {nota1} - Segunda nota {nota2}')

if media == 10:
    print(f'O aluno obteve a média {media} - APROVADO COM DISTINÇÃO')
elif media >= 7:
    print(f'O aluno obteve a média {media} - APROVADO')
else:
    print(f'O aluno obteve a média {media} - ALUNO REPROVADO')
