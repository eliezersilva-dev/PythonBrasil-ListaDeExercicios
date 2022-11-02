"""
Eliezer Silva
Exercício 51
-------------
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.

obs: Na lista de exercícios disponível em https://wiki.python.org.br/EstruturaDeRepeticao
os exercício 49 e 51 se repetem.
"""
print()

print()
n_termo = int(input('Informe a quantidade de termos: '))
n1 = 1
n2 = 1
n1_lista = []
n2_lista = []
cont = 1
print('S = ', end='')

while cont <= n_termo - 1:
    print(n1, '/', n2, '+ ', end='')
    n1_lista.append(n1)
    n2_lista.append(n2)
    n1 += 1
    n2 += 2
    cont += 1

print(n1, '/', n2, ' = ', sum(n1_lista), '/', sum(n2_lista))
