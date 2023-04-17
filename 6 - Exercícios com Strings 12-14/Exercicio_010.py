"""
Eliezer Silva
Exercício 10
-------------
Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e
imprima-o na tela por extenso.

Obs: A implementação do código poderia ser feita atráves de uma lista de string onde seria acessada
pelo índice. Ex:

lista = ['zero', 'um', 'dois', 'três', 'noventa e nove']
numero = int(input('Insira um número: '))
print(f'Número por extenso: {lista[numero -1]}')

No entanto, há uma biblioteca capaz de realizar essa tarefa de maneira mais simples e econômica. Optei por
essa solução...
"""

# pip install num2words
from num2words import num2words

print()

numero = int(input('Digite um número: '))
num_ptbr = num2words(numero, lang='pt-br')
print(f'Número por extenso: {num_ptbr}')




