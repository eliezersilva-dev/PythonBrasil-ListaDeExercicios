"""
Eliezer Silva
Exercício 19
-------------
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

print('Digite dez valores entre 0 e 1000.')

lista = []


def conjunto():
    contador = 1
    while contador <= 10:
        variavel = int(input('Digite um valor: '))

        if variavel < 0 or variavel > 100:
            print('Digite um valor entre 0 e 1000.')
            conjunto()
        else:
            lista.append(variavel)
        contador += 1


conjunto()

print(max(lista))
print(min(lista))
print((max(lista) + (min(lista))))