"""
Eliezer Silva
Exercício 12
------------
Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres
embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação
possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa
baixa, independentemente de como foram digitados.
"""
import random

print()


def retorna_palavra(palavra_embaralhada):
    print(f'Palavra embaralhada: {palavra_embaralhada}')
    print()
    continuar = input('Continuar? [s/n]: ')
    if continuar == 's':
        print()
        insere_palavra()
    else:
        print('Logout...')
        quit()


def embaralha_palavra(palavra):
    palavra = palavra.upper()
    palavra_embaralhada = random.sample(palavra, k=len(palavra))
    palavra_embaralhada = str(palavra_embaralhada)
    palavra_embaralhada = palavra_embaralhada.replace("'", '')
    palavra_embaralhada = palavra_embaralhada.replace(',', '')
    palavra_embaralhada = palavra_embaralhada.replace(' ', '')
    palavra_embaralhada = palavra_embaralhada.replace('[', '')
    palavra_embaralhada = palavra_embaralhada.replace(']', '')
    retorna_palavra(palavra_embaralhada)


def insere_palavra():
    palavra = input('Insira uma palavra: ')
    embaralha_palavra(palavra)


insere_palavra()
