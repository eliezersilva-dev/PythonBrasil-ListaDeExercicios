"""
Eliezer Lucas
Exercício 23
-------------
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""
print()

# numero = int(input('Digite um numero inteiro: '))
# lista = list(range(1, numero + 1))
# print(lista)
# nun_divisoes = 0
# lista_nao_primos = []
# lista_primos = []
# primo = True
#
# for i in lista:
#     if numero % i == 0:
#         primo = False
#         lista_nao_primos.append(i)
#
#     else:
#         lista_primos.append(i)
#
# print(f'O números primos entre 1 e {numero} são: {lista_primos}')
# print(f'Foram realizadas {nun_divisoes} divisões.')

numero = int(input('Digite um número: '))
lista_primos = []
divisoes = 0

for i in range(numero + 1):
    if i % 2 == 1 and i != 2:
        lista_primos.append(i)
        divisoes += 1
    else:
        divisoes += 1
print(f'Números primos entre  1 e {numero}: {lista_primos}')
print(f'Número de divisões: {divisoes}')
