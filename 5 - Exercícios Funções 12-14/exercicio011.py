"""
Eliezer Silva
Exercício 11
-------------
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no
formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""
print()

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']


def formatar_data():
    data_input = input('Insira data [dd/mm/aaaa]: ')
    data_format = data_input.replace('/', '')
    mes_format = int(data_format[2:4])
    dia_format = int(data_format[0:2])

    if dia_format > 31:
        print('Não existe dia maior que 31. Insira um dia válido.')
        formatar_data()
    elif dia_format > 30 and mes_format == 2 or mes_format == 4 or mes_format == 6 or mes_format == 9 or mes_format == 11:
        print('O mês informado não possui 31 dias. Insira uma data válida')
        formatar_data()
    elif mes_format > 12:
        print('Não existe mês maior que 12. Insira uma data válida')
        formatar_data()

    print()
    print('Data formatada:')
    print(f'{data_format[0:2]} de {meses[mes_format-1]} de {data_format[4:8]}')
    print()

    continuar = input('Repetir? [s/n]: ')
    if continuar == 's':
        formatar_data()
    else:
        print('Logout...')
        quit()


formatar_data()
