"""
Eliezer Silva
Exercício 17
-------------
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120
"""

numero = int(input("Fatorial de: "))
resultado = 1
contador = 1

while contador <= numero:
    resultado *= contador
    contador += 1

print(resultado)
