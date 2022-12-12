"""
Eliezer Silva
Exercício 05
-------------
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""

print()


def soma_imposto(taxa_imposto, custo):
    preco_final = custo + ((custo / 100) * taxa_imposto)
    preco_final = str(preco_final)
    preco_final = preco_final.replace('.', ',')
    print(f'Preço final: R$ {preco_final}', end='0')


def insere_preco():
    custo = int(input('Insira o valor: R$ '))
    taxa_imposto = int(input('Insira a taxa de imposto [%]: '))
    soma_imposto(taxa_imposto, custo)


insere_preco()
