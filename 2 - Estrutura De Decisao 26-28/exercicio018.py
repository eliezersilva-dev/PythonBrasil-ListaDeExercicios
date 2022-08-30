"""
Eliezer Silva
Exercício 18
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
_______________________________

Lógica do problema. Preciso verificar se:

Se o dia é entre 1 e 31;
Se o mês é entre 1 e 12;
Se mês for 04, 06, 09 ou 11, dia pode ser no máximo 30;
Se mês for 02, dia pode ser no máximo 28;
Se ano for bissexto e mês for 02, dia pode ser no máximo 29;

"""

print()
print('-'*20 + ' Vericador de Data '+'-'*20)
print()


data_input = input('Digite a data [dd/mm/aaaa]: ')
print()
data = data_input


# verificando validade do input - quantidade de caracteres
if len(data) != 10:
    print(f'A data {data_input} NÃo é uma data Válida.\n'
          f'Digite um valor válido [dd/mm/aa].')
    quit()


# verificar formato - se existe '/' na posição certa
if data[2] != '/' or data[5] != '/':
    print(f'A data {data_input} NÃo está com formato Válido.\n'
          f'Digite [dd/mm/aaaa].')
    quit()
# formatar formato - retirar '/'
else:
    data = data.replace('/', '')


# verificando se o input é numérico
if not data.isnumeric():
    print(f'A data {data_input} NÃo é uma data Válida.\n'
          f'Digite um valor válido [dd/mm/aa].')
    quit()


# 2º verificão validade do input - quantidade de caracteres
if len(data) != 8:
    print(f'A data {data_input} NÃo é uma data Válida.\n'
          f'Digite um valor válido [dd/mm/aa].')
    quit()


# separando valores dia - mês - ano
dia = int(data[0:2:1])
mes = int(data[2:4:1])
ano = int(data[4:8:1])
data_final = str('')


# validando dia
if not dia >= 1 or not dia <= 31:
    print(f'Data {data_input} inválida. Dia maior que 31.')
    quit()


# validando mês - exceto mes 02
if not mes >= 1 or not mes <= 12:
    print(f'A data {data_input} contém mês inválido.')
    quit()

if mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia == 31:
    print(f'A data {data_input} NÃO é uma data Válida.\n'
          f'O mês {mes} não possui {dia} dias')
    quit()


# verificando se o é ano bissexto
ano_bissexto = False
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            ano_bissexto = True
        else:
            ano_bissexto = False
    else:
        ano_bissexto = True
else:
    ano_bissexto = False


# validando mês 02
if mes == 2 and dia > 29:
    print(f'A data {data_input} Não é Válida.\n'
          f'O mês 02 deve conter 29 dias no máximo.')
    quit()
else:
    if mes == 2 and dia == 29 and ano_bissexto == False:
        print(f'A data {data_input} Não é Válida.\n'
              f'O ano {ano} não é bissexto, portando\n'
              f'o mês 02 deveria não deveria conter 29 dias.')
        quit()


print(f'A data {data_input} é uma data Válida.')

