"""
Eliezer Silva
Exercicio 11
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo.
- a soma do triplo do primeiro com o terceiro.
- o terceiro elevado ao cubo.
"""
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
numero_3 = int(input('Digite o terceiro número: '))

operacao1 = int((numero_1 * 2) + (numero_2 / 2))
operacao2 = int((numero_1 * 3) + numero_3)
operacao3 = float(numero_3 ** 3)

print(f'O produto do dobro do primeiro número com metade do segundo número é igual à: {operacao1}')
print(f'A soma do triplo do primeiro número com o terceiro número é igual à: {operacao2}')
print(f'O terceiro número elevado ao cubo é igual à: {operacao3:.1f}')
