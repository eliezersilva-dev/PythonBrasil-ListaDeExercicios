"""
Eliezer Silva
Exercício 05
_____________

Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""

print()
print('-' * 10 + ' Crescimento demográfico ' + '-' * 10)
print()


def crescimento_demografico():

    try:
        pais_a = float(input('Informe a população do país A: '))
        input_taxa_a = float(input('Informe a taxa de crescimento anual [%]: '))
        print()
        taxa_a = round((pais_a / 100) * input_taxa_a)

        pais_b = float(input('Informe a população do país B: '))
        input_taxa_b = float(input('Informe a taxa de crescimento anual [%]: '))
        print()
        taxa_b = round((pais_b / 100) * input_taxa_b)

        if pais_a > pais_b:
            print('A população do país A já é maior ou igual\n'
                  'à população do país B.')
            quit()

        if taxa_b > taxa_a:
            print('A taxa de crescimento do país B é maior que\n'
                  'a taxa de crescimento do país A.\n'
                  'Nesse caso a população do país A nunca alcançará\n'
                  'a população do país B.')
            quit()

        contador_anos = 0

        while pais_a <= pais_b:
            pais_a += taxa_a
            pais_b += taxa_b
            contador_anos += 1

        print(f' O país A levará cerca de {contador_anos} anos\n '
              f'para alcançar a marca de {int(pais_a)} habitantes\n '
              f'ultrapassando assim o país B que alcançará no mesmo\n '
              f'período a marca de {int(pais_b)} habitantes.')
        print()

    except ValueError:
        print('Digite apenas valores válidos.')
        print()
        crescimento_demografico()

    def continuar():
        continua = input('Dejesa repetir? [S/N]: ')
        print()
        continua = continua.upper()
        if continua != 'S' and continua != 'N':
            continuar()
        if continua == 'N':
            print('Finalizando...')
            quit()
        if continua == 'S':
            crescimento_demografico()

    continuar()


crescimento_demografico()
