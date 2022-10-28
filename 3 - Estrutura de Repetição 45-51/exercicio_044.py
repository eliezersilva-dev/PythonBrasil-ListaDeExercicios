"""
Eliezer Silva
Exercício 44
-------------
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos.
Para finalizar o conjunto de votos tem-se o valor zero.
"""
print()
print('-' * 10 + ' Eleição ' + '-' * 10)
print()

print('Para votar escolha o código do candidato:\n'
      '1 - João\n'
      '2 - José\n'
      '3 - Maria\n'
      '4 - Rose\n'
      '5 - Voto em Branco\n'
      '6 - Voto Nulo')

print()

joao1 = 0
jose2 = 0
maria3 = 0
rose4 = 0
branco5 = 0
nulo6 = 0

eleicao = True
total_votos = -1

while eleicao:
    voto = input('Informe o código do candidato.\n'
                 'Digite [fim] para finalizar.\n'
                 'Opção: ')
    total_votos += 1

    print()

    if voto == '1':
        joao1 += 1
    elif voto == '2':
        jose2 += 1
    elif voto == '3':
        maria3 += 1
    elif voto == '4':
        rose4 += 1
    elif voto == '5':
        branco5 += 1
    elif voto == '6':
        nulo6 += 1
    elif voto == 'fim':
        eleicao = False
    else:
        print('CÓDIGO INVÁLIDO.\n'
              'Escolha um código válido.')

print()
print('RESULTADO:')
print()
print(f'Candidato João : {joao1} voto(s)\n'
      f'Candidato José: {jose2} voto(s)\n'
      f'Candidata Maria: {maria3} voto(s)\n'
      f'Candidata Rose: {rose4} voto(s)')

print()
print(f'Total de votos: {total_votos}')
print()
print(f'Voto(s) em branco: {branco5}')
porcentagem_branco = (branco5 / total_votos) * 100
print(f'Porcentagem de votos em branco sobre o total de votos: {porcentagem_branco:.2f}%')
print()
print(f'Voto(s) nulo(s): {nulo6}')
porcentagem_nulo = (nulo6 / total_votos) * 100
print(f'Porcentagem de votos nulos sobre o total de votos: {porcentagem_nulo:.2f}%')
