"""
Eliezer Silva
Exercício 12
-------------
Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem
altura inferior à média de altura desses alunos.
"""
import random

print()


# construindo o dicionário de alunos, idade e altura
alunos = {}
contagem_alunos = 1
for i in range(0, 30):
    alunos[f'Aluno_{contagem_alunos}'] = int(random.randint(1, 18)), round(random.uniform(1, 3), 2)
    contagem_alunos += 1


# calculando a média de altura
media_altura = []
for i, j in alunos.values():
    media_altura.append(j)

media_altura = sum(media_altura) / len(media_altura)


# verificação dos requisitos : maior de 13 anos com altura inferior à média de altura
alunos_selecionados = []
for aluno, dados in alunos.items():
    variavel = [dados]
    for idade, altura in variavel:
        if altura < media_altura and idade > 13:
            alunos_selecionados.append(aluno)


# retornando resultados
print('Alunos    Idade   Altura')
for i in alunos.items():
    print(i)
print()
print(f'A média de altura dos alunos é de {media_altura:.2f} m')
print()
print(f'O(s) aluno(s) com idade maior que 13 anos e altura abaixo da média é(são):\n'
      f'{alunos_selecionados}')

