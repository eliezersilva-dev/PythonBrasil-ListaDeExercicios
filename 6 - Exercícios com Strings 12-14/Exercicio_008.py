"""
Eliezer Silva
Exercício 09
-------------
Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou
vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
"""
print()

termo = input('Digite uma palavra ou frase: ')

termo = termo.upper()
termo_inverso = termo[::-1]
termo_sem_espaco = termo.replace(' ', '')
termo_sem_espaco_inverso = termo_inverso.replace(' ', '')

print(f'Termo digitado: {termo}')
print(f'Termo digitado inverso: {termo_inverso}')

if termo_sem_espaco == termo_sem_espaco_inverso:
    print('O termo digitado é um Palíndrono.')
else:
    print('O termo digitado não é um Palídrono.')
