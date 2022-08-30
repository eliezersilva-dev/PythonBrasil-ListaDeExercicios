"""
Eliezer Silva
Exercício 21
-------------

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
quatro notas de 10, uma nota de 5 e quatro notas de 1.

# Não foram tratados os erros :)
"""

# Cabeçalho do Programa
print()
print('-'*10 + ' Caixa Eletrônico '+'-'*10)
print()

print('Saque mínimo R$ 10,00 - Saque máximo R$ 600,00')
print()

# Pegando o valor do input
saque = float(input('Informe o valor do saque: '))

# String final
resultado = f'O saque será de:\n'

# Separando o valor em notas
notas_100 = int((saque / 100))
notas_50 = int((saque % 100) / 50)
notas_10 = int(((saque % 100) % 50) / 10)
notas_5 = int((((saque % 100) % 50) % 10) / 5)
notas_1 = int((((saque % 100) % 50) % 10) % 5)

# Configurando String final
if notas_100 != 0:
    resultado += f'  {int(notas_100)} nota(s) de R$ 100,00\n'
if notas_50 != 0:
    resultado += f'  {int(notas_50)} nota(s) de R$ 50,00\n'
if notas_10 != 0:
    resultado += f'  {int(notas_10)} nota(s) de R$ 10,00\n'
if notas_5 != 0:
    resultado += f'  {int(notas_5)} nota(s) de R$ 5,00\n'
if notas_1 != 0:
    resultado += f'  {int(notas_1)} nota(s) de R$ 1,00'

# Sáida final
print(resultado)
