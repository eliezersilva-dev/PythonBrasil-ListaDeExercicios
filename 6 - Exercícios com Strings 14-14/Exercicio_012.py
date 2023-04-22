"""
Eliezer Silva
Exercício 12
-------------
Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso
deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço
separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
"""
import re
print()
print('Valida e corrige número de Telefone')
print()

telefone = input('Insira o telefone: ')
telefone_formatado = ''

padrao1 = re.compile(r'([0-9]{3,4}[-][0-9]{4})')  # cria padrao
padrao2 = re.compile(r'([0-9]{7,8})')  # cria padrao

var1 = padrao1.findall(str(telefone))  # procura e armazena padrao
var1 = ''.join(var1)  # converter list em str

var2 = (padrao2.findall(str(telefone)))  # procura e armazena padrao
var2 = ''.join(var2)  # converter list em str

# validações da entrada
if var1 == telefone:
    print(f'Telefone {telefone} válido. ')
elif var2 == telefone and len(telefone) == 7:
    telefone_formatado = str('3' + telefone)
    print(f'Telefone {telefone} possui 7 dígitos. Vou acrescentar o dígito 3 na frente: {telefone_formatado}')
    if len(telefone_formatado) == 8:
        telefone_formatado2 = str(telefone_formatado[0:4] + '-' + telefone[3:])
        print(f'Telefone {telefone_formatado} formatado para {telefone_formatado2}')
elif var2 == telefone and len(telefone) == 8:
    telefone_formatado = str(telefone[0:4] + '-' + telefone[4:])
    print(f'Telefone {telefone} formatado para {telefone_formatado}')
else:
    print('Telefone inválido.')
