"""
Elizer Silva
Exercício 09
------------
Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

Obs: Para calcular a verificação utilizei o cálculo demostrado em:
https://campuscode.com.br/conteudos/o-calculo-do-digito-verificador-do-cpf-e-do-cnpj
"""
print()


def verificacao(digito, digito_verificado):

    if digito == digito_verificado:
        print('CPF Válido!')
        print()
    else:
        print('CPF Inválido!')
        print()

    continuar = input('Inserir outro CPF? [s/n]: ')

    if continuar == 's':
        cpf_entrada()
    else:
        print()
        print('Finalizando...')
        quit()


def calcular_digitos(entrada_cpf, digito):

    # Verificação primeiro dígito
    lista_calcular = [10, 9, 8, 7, 6, 5, 4, 3, 2]

    verificar_digito_um = list(zip(entrada_cpf, lista_calcular))
    digito_um = []

    for i, j in verificar_digito_um:
        digito_um.append(i * j)

    digito_um = sum(digito_um)
    digito_um = digito_um % 11
    digito_um = 11 - digito_um

    if digito_um >= 10:
        digito_um = 0

    # Verificação segundo dígito
    entrada_cpf.append(digito_um)
    lista_calcular.insert(0, 11)

    verificar_digito_dois = list(zip(entrada_cpf, lista_calcular))
    digito_dois = []

    for i, j in verificar_digito_dois:
        digito_dois.append(i * j)

    digito_dois = sum(digito_dois)
    digito_dois = digito_dois % 11
    digito_dois = 11 - digito_dois

    if digito_dois >= 10:
        digito_dois = 0

    digito_verificado = str(digito_um) + str(digito_dois)

    verificacao(digito, digito_verificado)


def cpf_entrada():

    cpf = input('Insira um CPF [xxx.xxx.xxx-xx]: ')

    entrada = cpf
    entrada = entrada.replace('.', '')
    entrada = entrada.replace('-', '')

    if len(entrada) < 11:
        print('CPF inválido.')
        cpf_entrada()

    entrada_cpf = []
    for indice in entrada:
        entrada_cpf.append(int(indice))

    digito = entrada[len(entrada)-2: len(entrada)]


    calcular_digitos(entrada_cpf, digito)


cpf_entrada()
