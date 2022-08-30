"""
Eliezer Silva
Exercício 20
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular
a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

print()
print('-'*20 + ' Calcular média '+'-'*20)
print()
try:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))

    media = (nota1 + nota2 + nota3) / 3

    if media < 7:
        print(f'Média {media}: Aluno REPROVADO.')
    if 7 <= media <= 9:
        print(f'Média {media}: Aluno APROVADO.')
    if media == 10:
        print(f'Média {media}: Aluno APROVADO COM DISTINÇÃO.')
except:
    print('erro: Digite uma nota válida.')
