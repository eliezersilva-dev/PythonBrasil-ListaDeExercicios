"""
Eliezer Silva
Exercício 17
-------------
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado
pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado
quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""
print()
print('-' * 10 + ' Competição de Salto ' + 10 * '-')
print()

atletas = []


def resultado():
    for i, j in atletas:
        print(f'Atleta: {i}')
        print()
        n = []
        for k in j:
            n = j
        print(f'Primeiro salto: {n[0]} m\n'
              f'Segundo salto: {n[1]} m\n'
              f'Terceiro salto: {n[2]} m\n'
              f'Quarto salto: {n[3]} m\n'
              f'Quinto salto: {n[4]} m')
        print()

        print(f'Melhor salto: {max(n)} m\n'
              f'Pior salto: {min(n)} m')
        n.sort()
        n.pop(0)
        n.pop(-1)
        media = sum(n) / len(n)
        print(f'Média dos demais saltos: {media:.2f} m')
        print()
        print(f'Resultado Final:\n'
              f'{i}: {media:.2f} m')
        print()
        print('-'*20)
        print()
    quit()


def continuar():
    continua = input('Adicionar atleta? [s/n]: ')
    continua = continua.upper()
    if continua == 'S':
        print()
        criar_atletas()
    if continua == 'N':
        print()
        print('-' * 20)
        print('|'+'     RESULTADO    '+'|')
        print('-' * 20)
        print()
        resultado()
    else:
        print('...')
        continuar()


def criar_atletas():
    nome = input('Nome do atleta: ')
    cont = 1
    saltos = []
    while cont <= 5:
        try:
            valor = float(input(f'Salto {cont}: '))
            if valor < 0:
                print(f'Informe uma valor válido.\n'
                      f'Refaça a operação.')
                print()
                criar_atletas()
            else:
                saltos.append(valor)
        except ValueError as e:
            print(f'Error: {e}\n'
                  f'Refaça a operação.')
            print()
            criar_atletas()
        cont += 1
    atleta = [nome] + [saltos]
    atletas.append(atleta)
    print()
    continuar()


criar_atletas()
