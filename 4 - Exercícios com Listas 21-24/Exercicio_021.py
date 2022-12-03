"""
Eliezer Silva
Exercício 21
--------------

Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um
litro de combustível. Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros
e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo.
O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada
execução do programa.

Comparativo de Consumo de Combustível

Veículo 1
Nome: Fusca
Km por litro: 7
Veículo 2
Nome: Gol
Km por litro: 10
Veículo 3
Nome: Uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - Fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - Gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - Uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - Vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - Peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do Peugeout.

obs: Apesar de o exercício pedir que se carregue DUAS listas (veículos e consumo), optei por usar uma solução diferente
na qual foi usado dicionário(dict). Tal abordagem foi escolhida por duas causas, a primeira é porque acredito se mais
eficiente e a segunda se por que a abordagem de suas listas (referenciando o indíce uma da outra) foi usado no exercíco
anterior.
"""
print()
print('Comparativo de Consumo de Combustível')
print()

veiculos_consumo = {}


def resultado():
    print()
    print('Relatório Final')
    menor_consumo = 'eita'
    indice = 1
    for i, j in veiculos_consumo.items():
        print(f'{indice} - {i} - {j} - {(1000/j):.2f} litros - R$ {((1000/j)*2.25):.2f}')
        indice += 1
        if j == max(veiculos_consumo.values()):
            menor_consumo = i
    print(f'O menor consumo é do {menor_consumo}')


def insira_veiculos():
    cont = 1
    while cont < 6:
        carro = input(f'Veículo {cont}\n'
                      f'Nome: ')
        km_litro = float(input('Km por litro: '))
        veiculos_consumo.update({f'{carro}': km_litro})
        cont += 1
    resultado()


insira_veiculos()
