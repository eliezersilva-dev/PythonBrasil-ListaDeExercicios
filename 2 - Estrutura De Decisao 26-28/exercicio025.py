"""
Eliezer Silva
Exercício 25
-------------
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

print()
print('-' * 10 + ' Inocente ou Culpado ' + '-' * 10)
print()

resultado = 0

print('Responda as perguntas.')
print()

resposta = input('Telefonou para a vítima? [s/n]: ')
if resposta != 's' and resposta != 'n':
    print('Digite uma resposta válida: [s/n]')
    quit()
if resposta == 's':
    resultado += 1

resposta = input('Esteve no local do crime? [s/n]: ')
if resposta != 's' and resposta != 'n':
    print('Digite uma resposta válida: [s/n]')
    quit()
if resposta == 's':
    resultado += 1

resposta = input('Mora perto da vítima? [s/n]: ')
if resposta != 's' and resposta != 'n':
    print('Digite uma resposta válida: [s/n]')
    quit()
if resposta == 's':
    resultado += 1

resposta = input('Devia para a vítima? [s/n]: ')
if resposta != 's' and resposta != 'n':
    print('Digite uma resposta válida: [s/n]')
    quit()
if resposta == 's':
    resultado += 1

resposta = input('Já trabalhou com a vítima? [s/n]: ')
if resposta != 's' and resposta != 'n':
    print('Digite uma resposta válida: [s/n]')
    quit()
if resposta == 's':
    resultado += 1

print()

if resultado == 5:
    print('Classificado como: ASSASSINO.')
elif resultado == 4 or resultado == 3:
    print('Classificado como: CÚMPLICE.')
elif resultado == 2 or resultado == 1:
    print('Classificado como: SUSPEITO.')
else:
    print('Classificado como: INOCENTE.')
