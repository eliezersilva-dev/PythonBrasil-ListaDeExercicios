"""
Eliezer Silva
Exercício 09
-------------
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""

lista = list(range(1, 50, 1))
lista_impar = []
for i in lista:
    if i % 2 != 0:
        lista_impar.append(i)

print(lista_impar)
