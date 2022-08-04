"""
Eliezer Silva
Exercício 17

Faça um Programa que peça um número correspondente a um determinado ano e
em seguida informe se este ano é ou não bissexto.

Para determinar se um ano é bissexto, execute estas etapas:
1- Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
2- Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
3- Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
4- O ano é bissexto (tem 366 dias).
5- O ano não é um ano bissexto (tem 365 dias).
Método de cáclulo retirado de:
https://docs.microsoft.com/pt-br/office/troubleshoot/excel/determine-a-leap-year
"""

print()
ano = int(input('Informe o ano: '))
print()

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O ano {ano} é bissexto portanto possui 366 dias.')
        else:
            print(f'O ano {ano} não é bissexto portanto possui 365 dias.')
    else:
        print(f'O ano {ano} é bissexto portanto possui 366 dias.')
else:
    print(f'O ano {ano} não é bissexto portanto possui 365 dias.')
