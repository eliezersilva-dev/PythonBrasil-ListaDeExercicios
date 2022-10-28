"""
Eliezer Silva
Exercício 45
-------------
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com
o gabarito da prova e assim calcular o total de acertos e a nota
(atribuir 1 ponto por resposta certa).
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar
o sistema. Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.

Gabarito da Prova:
01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite
o gabarito da prova antes dos alunos usarem o programa.
"""

print()
print('-'*10+' Prova '+'-'*10)
print()

gabarito = {'01': 'A', '02': 'B', '03': 'C', '04': 'D', '05': 'E',
            '06': 'E', '07': 'D', '08': 'C', '09': 'B', '10': 'A'}

# print('Professor, digite o gabarito da prova.')
# gabarito = {}
# questoes = 1
# cont = 0
#
# while cont < 10:
#     resposta = input(f'Resposta questão 0{questoes}: ')
#     resposta = resposta.upper()
#     gabarito.update({f'0{questoes}': resposta})
#     questoes += 1
#     cont += 1
# print()

alunos = {}
contagem_aluno = 1
continuar = True

while continuar:
    alunos.update({f'Aluno{contagem_aluno}': 0})
    pontos_aluno = 0

    for i, j in gabarito.items():
        resposta = input(f'Questão {i}: ')
        resposta = resposta.upper()
        if resposta == j:
            pontos_aluno += 1
            alunos[f'Aluno{contagem_aluno}'] = pontos_aluno
    contagem_aluno += 1

    print()
    continuar = input('Continuar? [s/n]: ')
    if continuar == 'n':
        print('Finalizando...')
        print()
        continuar = False
    else:
        print('Continuando...')
        print()
        pass

print('Resultado:')
for i, j in alunos.items():
    print(f'{i} nota: {j}')
print()

total_alunos = len(alunos.keys())
print(f'Total de alunos: {total_alunos} alunos')

maior_nota = max(alunos.values())
aluno_maior = ''
for i, j in alunos.items():
    if j == maior_nota:
        aluno_maior = i
        break
print(f'Maior nota: {aluno_maior} Nota: {maior_nota}')

menor_nota = min(alunos.values())
aluno_menor = ''
for i, j in alunos.items():
    if j == menor_nota:
        aluno_menor = i
        break
print(f'Menor nota: {aluno_menor} Nota: {menor_nota}')

media = sum(alunos.values()) / total_alunos
print(f'Média de notas da turma: {media:.2f}')
