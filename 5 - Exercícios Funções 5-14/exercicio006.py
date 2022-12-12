"""
Eliezer Silva
Exercício 06
-------------
Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as
vezes que desejar.
"""
print()

hora_a = 0
hora_p = 0
minuto = 0


def saida():
    print(f'{hora_a}:{minuto} A.M.')
    print(f'{hora_p}:{minuto} P.M')
    print()
    continuar = input('Continuar [s/n]: ')
    if continuar == 'n':
        pass
    if continuar == 's':
        print()
        conversao()


def conversao():
    global hora_a
    global hora_p
    global minuto

    hora = int(input('Insira a hora: '))
    minuto = int(input('Insira o minuto: '))

    if hora > 12:
        hora_p = hora
        hora_a = hora - 12
    if hora < 12:
        hora_a = hora
        hora_p = hora + 12
    if hora == 12:
        hora_a = hora
        hora_p = 00

    print()
    saida()


conversao()
