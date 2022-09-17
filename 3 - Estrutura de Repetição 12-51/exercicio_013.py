"""
Eliezer Silva
Exercício 13
_____________
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""

valor1 = int(input('Digite o primeiro número:  '))
valor2 = int(input('Digite o segundo número:  '))
potenciacao = valor1 ** valor2
print(f'{valor1} elevado a {valor2} = {potenciacao}')
