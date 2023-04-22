"""
Eliezer Silva
Exercício 13
-------------
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com
as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o
usuário ganhou ou perdeu o jogo.
Obs: As palavras para testar o código foram colocadas em uma variável. No entanto, foi
incluído uma linha (comentada) para a leitura das palavras em um arquivo como pede o exercício.
"""
import random

print()
print('-' * 5 + ' JOGO DAS PALAVRAS EMBARALHADAS ' + '-' * 5)
print()
print('REGRAS:\n'
      'Descubra a palavra para ganhar.\n'
      'Se errar seis vezes você perde.')
print()
print('-' * 42)
print()

# Para ler as palavras em um arquivo .txt
# with open ('caminho/arquivo.txt, 'r', encoding='utf8') as arquivo:
# palavra = arquivo.read()


def chamar_jogo():
    lista_palavras = (['abacate', 'bicicleta', 'cadeira', 'dentes', 'elefante',
                       'festar', 'guitarra', 'ilhota', 'jornal', 'computador'])
    palavra = random.choice(lista_palavras)
    cont_erros = 0

    palavra_embaralhada = random.sample(palavra, k=len(palavra))  # metodo sample() retorna random não repetidos
    palavra_embaralhada = ''.join(palavra_embaralhada)  # converte list em str

    while cont_erros < 6:
        print(f'Total de erros: [{cont_erros}]')
        print(f'Palavra embaralhada: {palavra_embaralhada}')
        tentativa = input('Qual é a palavra? :')
        tentativa = tentativa.replace(' ', '')  # retira espaços do input
        print(f'Sua tentativa: {tentativa}')
        if tentativa == palavra:
            print('Parabéns!! Você acertou (˘◡˘)')
            print()
            continuar = input('Quer jogar outra vez [s/n]? ')
            continuar = continuar.lower()
            if continuar == 's':
                print()
                chamar_jogo()
            else:
                print()
                print('Ok! Até a próxima  (•◡•) /')
                quit()

        else:
            print('Ops! Você errou!')
            print()
            cont_erros += 1

    print(f'Total de erros: [{cont_erros}]')
    print('Você perdeu (ㆆ_ㆆ)')

    continuar = input('Jogar novamente [s/n]? ')
    continuar = continuar.lower()
    if continuar == 's':
        print()
        chamar_jogo()
    else:
        print()
        print('Ok! Até a próxima  (•◡•) /')


chamar_jogo()
