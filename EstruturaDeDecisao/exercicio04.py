"""
Eliezer Silva
Exercício 04
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = input('Digite uma letra: ')
letra = letra.upper()
vogais = ['A', 'E', 'I', 'O', 'U']
consoantes = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'L', 'K', 'M',
              'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'X', 'Z']

if letra in vogais:
    print(f'A letra {letra} é uma vogal.')
elif letra in consoantes:
    print(f'A letra {letra} é uma consoante.')
else:
    print(f'O caractere digitado não é uma letra.')
