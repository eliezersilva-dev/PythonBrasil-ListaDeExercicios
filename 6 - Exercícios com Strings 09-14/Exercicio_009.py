"""
Elizer Silva
Exercício 09
------------
Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.
"""

###### Não terminado...

def verificacao(entrada, digito):
    print(entrada)
    print(digito)


def cpf_entrada():

    cpf = '277.899.748-23'

    entrada = cpf
    entrada = entrada.replace('.', '')
    entrada = entrada.replace('-', '')

    if len(entrada) < 11:
        print('CPF inválido.')
        cpf_entrada()

    digito = entrada[len(entrada)-2: len(entrada)]

    entrada = list(entrada)
    digito = int(digito)

    verificacao(entrada, digito)


cpf_entrada()
