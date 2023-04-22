"""
Eliezer Silva
Exercício 14
-------------
Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como
números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma
subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e
afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras.
Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.

Obs: Leet é uma forma de substituição de caracteres. Para este exemplo optei pelas seguintes regras:
- Substituição das letras por caracteres correspondentes;
- Apenas um grupo de caracteres de substituição formado a partir da referência citada abaixo;
- Sinais de pontuação serão ignorados pela tradução.

Referência: https://pt.wikipedia.org/wiki/Leet
"""
print()
print('-'*10 + ' Tradutor Leet ' + '-'*10)
print()

letras = {
    'A': '4',
    'B': '8',
    'C': '(',
    'D': '[)',
    'E': '3',
    'F': '|=',
    'G': '6',
    'H': '/-/',
    'I': '1',
    'J': '_/',
    'K': '|<',
    'L': '|_',
    'M': '|\/|',
    'N': '/\/',
    'O': '0',
    'P': '|*',
    'Q': '9',
    'R': '|2',
    'S': '5',
    'T': '7',
    'U': '(_)',
    'V': 'V',
    'W': 'vv',
    'X': '><',
    'Y': 'j',
    'Z': '2'
    }

texto = input('Digite um texto: ')
texto_traduzido = ''

for i in texto.upper():
    if i in letras:
        texto_traduzido += (letras[i])
    elif i not in letras:
        texto_traduzido += i.lower()

print(f'Texto inseriro: {texto}')
print(f'Texto traduzido: {texto_traduzido}')
