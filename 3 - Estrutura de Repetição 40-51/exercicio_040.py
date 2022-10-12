"""
Eliezer Silva
Exercício 40
-------------
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999).
Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""


cod_cidades = []
n_veiculos = []
n_acidentes = []
acidentes_2000 = []

for i in range(5):
    print("\nCidade número ", i + 1)
    codigo_cidade = int(input("Digite o código da cidade: "))
    while codigo_cidade in cod_cidades:
        print("[Código já digitado]")
        codigo_cidade = int(input("Digite outro código: "))

    numero_acidentes = int(input("Digite o número de acidentes: "))
    numero_veiculos = int(input("Digite o número de veiculos: "))

    if numero_veiculos > 2000:
        acidentes_2000.append(numero_acidentes)
        n_acidentes.append(numero_acidentes)
    else:
        n_acidentes.append(numero_acidentes)

    n_veiculos.append(numero_veiculos)
    cod_cidades.append(codigo_cidade)

indice_acidentes_menor = n_acidentes.index(min(n_acidentes))
indice_acidentes_maior = n_acidentes.index(max(n_acidentes))

print("\nMenos acidentes\nQuantidade de acidentes: ", min(n_acidentes), "\nCódigo da cidade: ", cod_cidades[indice_acidentes_menor])
print("\nMais acidentes\nQuantidade de acidentes: ", max(n_acidentes), "\nCódigo da cidade: ", cod_cidades[indice_acidentes_maior])

media_veiculos = sum(n_veiculos) / len(n_veiculos)
print("\nMédia de veiculos nas 5 cidades: ", media_veiculos)

media_acidentes_2000 = sum(acidentes_2000) / len(acidentes_2000)
print("\nMédia de acidentes nas cidades com menos de 2000 veículos: ", media_acidentes_2000)
