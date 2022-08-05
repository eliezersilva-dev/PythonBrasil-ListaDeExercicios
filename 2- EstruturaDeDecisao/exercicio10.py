"""
Eliezer Silva
Exercício 10
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

nome = input('Qual o seu nome? ')
turno = input('Em que turno você estuda? \n'
              '[M] Matutino '
              '[V] Vespertino '
              '[N] Noturno: ')

turno = turno.upper()

if turno != 'M' and turno != 'V' and turno != 'N':
    print('Valor inválido.')
    exit()
else:
    if turno == 'M':
        print(f'Bom dia {nome}.')
    elif turno == 'V':
        print(f'Boa tarde {nome}.')
    elif turno == 'N':
        print(f'Boa noite {nome}.')
