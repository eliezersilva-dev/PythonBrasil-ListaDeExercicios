"""
Eliezer Silva
Exercício 11
-------------
Altere o programa anterior para mostrar no final a soma dos números.
"""

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

lista = [valor1, valor2]
variavel = list(range(lista[0], lista[1], 1))

variavel.remove(lista[0])

soma = 0
for i in variavel:
    soma += i

print(f'Os números que compreende o intervalo entre {valor1} e {valor2} são:\n'
      f'{variavel}\n'
      f'Sendo que a soma desses números é: {soma} ')
