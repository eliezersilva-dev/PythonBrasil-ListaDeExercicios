"""
Eliezer Silva
Exercício 45
------------
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa
que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe
a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois
calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem
da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome
do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
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


# Outra solução:
# atletas = []
# while True:
#     nome = input(
#         "Digite o nome do atleta (ou enter para encerrar o programa): "
#     )
#     if nome == "":
#         break
#     atleta = {
#         "nome": nome,
#         "saltos": [],
#         "media": 0,
#         "melhor_salto": 0,
#         "pior_salto": 0,
#     }
#     for i in range(5):
#         atleta.get("saltos").append(
#             float(input(f"Distância do {i+1}º salto: "))
#         )
#     atleta.get("saltos").sort()  # ? Ordena a lista
#     atleta["pior_salto"] = atleta.get("saltos").pop(0)
#     atleta["melhor_salto"] = atleta.get("saltos").pop()
#     atleta["media"] = sum(atleta.get("saltos")) / 3
#     print(
#         f"\nMelhor salto: {atleta.get('melhor_salto'):.1f} m"
#         f"\nPior salto: {atleta.get('pior_salto'):.1f} m"
#         f"\nMédia dos demais saltos: {atleta.get('media'):.1f} m\n"
#     )
#     atletas.append(atleta)
#
# print("\n\nResultado final")
#
# for atleta in atletas:
#     print(f"{atleta.get('nome')}: {atleta.get('media'):.1f} m")
