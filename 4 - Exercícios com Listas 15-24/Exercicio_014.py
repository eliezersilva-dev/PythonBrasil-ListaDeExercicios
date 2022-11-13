"""
Eliezer Silva
Exercício 14
-------------
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa
no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
import time

print()
print('-'*5+' Interrogatório '+5*'-')
print()
print('Responda as perguntas:')
print()

perguntas = ['Telefonou para a vítima?', 'Esteve no local?', 'Mora perto da vítima?',
             'Devia para a vítima?', 'Já trabalhou para vítima?']
respostas = 0


def interroga():
    global respostas
    for pergunta in perguntas:
        resposta = input(f'{pergunta} [s/n]: ')
        resposta = resposta.upper()

        if resposta == 'S':
            respostas += 1
            print()
        elif resposta == 'N':
            print()
        else:
            print('Para resposta digite [s] para Sim ou [n] para Não.')
            interroga()


interroga()

print('Analisando as respostas...')
time.sleep(3)
print('Analisando as respostas...')
time.sleep(3)
print('Analisando as respostas...')
time.sleep(3)
print('Analisando as respostas...')
time.sleep(3)

if respostas == 1 or respostas == 0     :
    print('Inocente.')
if respostas == 2:
    print('Suspeita.')
if respostas == 3 or respostas == 4:
    print('Cúmplice.')
if respostas == 5:
    print('ASSASSINO!!!.')
