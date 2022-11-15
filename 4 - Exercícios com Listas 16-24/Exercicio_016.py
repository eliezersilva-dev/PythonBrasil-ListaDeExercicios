"""
Eliezer Silva
Exercício 16
-------------
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor
que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes
intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

obs: Para atender o desafio proposto neste exercício (não usar ifs aninhados) precisei
buscar solução na internet. Trago a solução que julguei mais eficiente.
A lógica da solução foi proposta por Renzo do canal DevPro <a>https://www.youtube.com/watch?v=tZC0wuqoTnE</>.
"""

print()
print('Indíces dos intervalos de valores: \n'
      '1 - 200 - 299\n'
      '2 - 300 - 399\n'
      '3 - 400 - 499\n'
      '4 - 500 - 599\n'
      '5 - 600 - 699\n'
      '6 - 700 - 799\n'
      '7 - 800 - 899\n'
      '8 - 900 - 999\n'
      '9 - 1000 em diante')
print()

salarios = [200, 250, 320, 413, 516, 680, 791, 877, 999, 1000, 2000, 3000]

# esse trecho pode ser usado para dar a liberdade do usuário digitar os salários
# cont = 1
# while cont <= 10:
#   venda = (int(input(f'Venda do vendedor {cont}: ')))
#   salario = ((venda // 100) * 9) + 200
#   salarios.append(salario)
#   cont += 1

contagem_faixa_salarial = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for salario in salarios:
    indice = (salario // 100) - 2
    indice_maximo = len(contagem_faixa_salarial) - 1
    indice = min(indice, indice_maximo)
    contagem_faixa_salarial[indice] += 1

print('Salários:\n', salarios)
print()
print('Número de salário em cada intervalo de valores:')
cont_indice = 1
for i in contagem_faixa_salarial:
    print(f'intervalo {cont_indice} - Quantidade de salários: {i}')
    cont_indice += 1
