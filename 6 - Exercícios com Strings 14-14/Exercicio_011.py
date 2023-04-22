"""
Eliezer Silva
Exercício 11
-------------
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá
uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S

Obs: As palavras para testar o código foram colocadas em uma variável. No entanto, foi
incluído uma linha (comentada) para a leitura das palavras em um arquivo.
"""
import random

print()
print('-'*10 + ' JOGO DA FORCA ' + '-'*10)
print()
print('Descubra a palavra para ganhar.\n'
      'Se errar seis vezes você perde.')
print()
print('-'*35)
print()

# Para ler as palavras em um arquivo .txt
# with open ('caminho/arquivo.txt, 'r', encoding='utf8') as arquivo:
# palavra = arquivo.read()

lista = (['abacate', 'bicicleta', 'cadeira', 'dente', 'elefante',
         'festa', 'guitarra', 'ilha', 'jornal', 'computador'])
palavra = random.choice(lista)
entrada_usuario = ''
saida_usuario = '_'*len(palavra)
erros = 0


def chamar_letra():

    global erros
    global palavra
    global entrada_usuario
    global saida_usuario

    print(f'Palavra: {saida_usuario}')
    print(f'Letras digitadas: [{entrada_usuario}]')

    entrada = input('Digite uma letra: ')

    if entrada not in palavra:
        erros += 1
        print(f'Você errou pela {erros}º vez.')
        if erros == 6:
            print()
            print('Você perdeu.')
            continuar = input('Continuar? [s/n]: ')
            continuar = continuar.lower()
            if continuar == 's':
                palavra = random.choice(lista)
                entrada_usuario = ''
                saida_usuario = '_' * len(palavra)
                erros = 0
                chamar_letra()
            else:
                quit()

    entrada_usuario += entrada

    for i in palavra:
        if i in entrada_usuario:
            saida_usuario += i
        else:
            saida_usuario += '_'

    print()

    saida_usuario = saida_usuario[-len(palavra)::]

    for i in saida_usuario:
        if '_' not in saida_usuario:
            print('Parabéns!! Você venceu!')
            continuar = input('Continuar? [s/n]: ')
            continuar = continuar.lower()
            if continuar == 's':
                palavra = random.choice(lista)
                entrada_usuario = ''
                saida_usuario = '_' * len(palavra)
                erros = 0
                chamar_letra()
            else:
                quit()
        else:
            chamar_letra()


chamar_letra()
