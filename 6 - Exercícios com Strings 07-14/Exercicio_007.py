"""
Eliezer Silva
Exercício 07
-------------
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
- quantos espaços em branco existem na frase.
- quantas vezes aparecem as vogais a, e, i, o, u.
"""
print()

vogais = ['a', 'e', 'i', 'o', 'u']

frase = input('Insira uma frase (não use acentos): ')
frase = frase.lower()

espaco_branco = 0
qtda_vogais = 0

for i in frase:
    if i == ' ':
        espaco_branco += 1
    if i in vogais:
        qtda_vogais += 1

print(f'Na frase há {espaco_branco} espaços em branco.')
print(f'Na frase há {qtda_vogais} vogais.')
