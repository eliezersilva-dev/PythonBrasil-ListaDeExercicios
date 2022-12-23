"""
Eliezer Silva
Exercício 13
-------------
Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e
o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa
de forma elegante.
"""

print()


def desenhar_retangulo(altura, largura):
    contador = 0
    print('+' + '-' * largura + '+')
    while contador < altura:
        print('|' + ' ' * largura + '|')
        contador += 1
    print('+' + '-' * largura + '+')
    repetir = input('Repetir? [s/n]: ')
    if repetir == 's':
        inserir_valores()
    else:
        print('Logout...')
        quit()


def inserir_valores():
    altura = int(input('Insira a altura: '))
    if altura > 20:
        altura = 20
    largura = int(input('Insira a largura: '))
    if largura > 20:
        largura = 20

    desenhar_retangulo(altura, largura)


inserir_valores()
