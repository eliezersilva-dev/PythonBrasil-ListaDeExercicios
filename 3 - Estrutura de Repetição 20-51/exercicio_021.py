"""
Eliezer Silva
Exercício 21
-------------
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

numero = 9

lista = list(range(2, numero + 1, 1))
print(lista)

lista_primos = []

for i in lista:
    if numero / i == 1 and numero % i == 0:
        lista_primos.append(i)

print(lista_primos)


