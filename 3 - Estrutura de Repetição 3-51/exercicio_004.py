"""
Eliezer Silva
Exercício 04
------------

Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 30% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que
calcule e escreva o número de anos necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""

print()
print('-' * 10 + ' Crescimento demográfico ' + '-' * 10)
print()

pais_A = 80000
taxa_A = (80000 / 100) * 30

pais_B = 200000
taxa_B = (200000 / 100) * 1.5

contador = 0

while pais_A <= pais_B:
    pais_A += taxa_A
    pais_B += taxa_B
    contador += 1

print(f'O país A levará cerca de {contador} anos\n '
      f'para alcançar a marca de {int(pais_A)} habitantes\n '
      f'ultrapassando assim o país B que alcançará no mesmo\n '
      f'período a marca de {int(pais_B)} habitantes.')
