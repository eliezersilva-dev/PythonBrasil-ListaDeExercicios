"""
Eliezer Silva
Exercício 01
-------------
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""
print()

primeiro_termo = input('Insira a primeira palavra ou frase: ')
segundo_termo = input('Insira a segunda palavra ou frase: ')

print(f'Tamanho de {primeiro_termo}: {len(primeiro_termo)} caracteres.')
print(f'Tamanho de {segundo_termo}: {len(segundo_termo)} caracteres.')

if len(primeiro_termo) != len(segundo_termo):
    print('As duas strings não possuem os mesmos tamanhos.')
else:
    print('As duas strings possuem os mesmos tamanhos.')

if primeiro_termo != segundo_termo:
    print('As duas strings não possuem o mesmo conteúdo.')
else:
    print('As duas strings possuem o mesmo conteúdo.')
