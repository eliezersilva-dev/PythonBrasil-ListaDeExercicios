"""
Eliezer Silva
Exercício 12
-------------
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
"""

print()
print('-' * 10 + ' Tabuada ' + '-' * 10)
print()


def multiplicacao():

    tabuada = int(input('Digite um valor entre 1 e 10: '))
    print()

    try:
        if tabuada < 1 or tabuada > 10:
            print('Digite um valor válido.')
            print()
            multiplicacao()
    except ValueError:
        print('Erro. Digite um valor válido.')
        print()
        multiplicacao()

    print(f'Tabuada do {tabuada}')
    multiplica = list(range(0, 11, 1))

    for i in multiplica:
        print(f'{tabuada} x {i} = {i * tabuada}')
    print()

    def continuar():
        continua = input('Deseja continuar [S/N]: ')
        continua = continua.upper()

        if continua != 'S' and continua != 'N':
            print('Escolha S para sim ou N para não.')
            continuar()

        if continua == 'S':
            print()
            multiplicacao()
        if continua == 'N':
            print('Finalizando...')

    continuar()


multiplicacao()
