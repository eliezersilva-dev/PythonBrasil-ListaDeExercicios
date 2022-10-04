"""
Eliezer Silva
Exercício 32
-------------
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""
print()

numero = int(input('Fatorial de: '))

lista = list(range(1, numero+1))
lista.sort(reverse=True)

fatorial = 1
for i in lista:
    fatorial *= i

resultado_tela = str(lista)[1:-1]  # str(lista).strip('[]') - desempacotando itens da lista
resultado_tela = resultado_tela.replace(',', ' .')

print(f'{numero}! = {resultado_tela} = {fatorial}')
