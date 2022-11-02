"""
Eliezer Silva
Exercício 50
-------------
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
"""
print()

n1 = 1
n2 = 2
n_termos = int(input('Informe a quantidade de termos: '))
soma_n1 = [1]
soma_n2 = []

cont = 1
while cont <= n_termos - 1:
    soma_n1.append(n1)
    soma_n2.append(n2)
    n2 += 1
    cont += 1

resultado = str(soma_n2)
resultado = resultado.replace(',', '+/')
resultado = resultado.replace('/', '1/')
resultado = resultado.replace(' ', '')
resultado = resultado.replace('+', ' + ')
resultado = resultado.replace('[', '')
resultado = resultado.replace(']', '')

soma_n1 = sum(soma_n1)
soma_n2 = sum(soma_n2)
print(f'H = 1 +  {resultado} = {soma_n1}/{soma_n2}')
