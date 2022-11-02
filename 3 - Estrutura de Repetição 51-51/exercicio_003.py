"""
Eliezer Lucas
Exercício 03
_____________
Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

print()
print('-' * 10 + ' Dados de Usuário ' + '-' * 10)
print()


def valida_nome():
    nome = input('Digite o nome: ')
    nome_format = nome.replace(' ', '')

    if not nome_format.isalpha():
        print(f'O nome {nome} contém caracteres inválidos.\n'
              f'Digite novamente.')
        print()
        valida_nome()
    else:
        return nome

    if len(nome_format) < 3:
        print('Não é permitido nome com menos de três letras.\n'
              'Digite o nome novamente.')
        print()
        valida_nome()
    else:
        return nome


def valida_idade():
    idade = (input('Digite a idade: '))

    try:
        idade = int(idade)
    except ValueError:
        print('Digite apenas números para a idade.')
        print()
        valida_idade()

    if idade < 1 or idade > 150:
        print('A idade deve conter um valor entre 1 e 150.')
        print()
        valida_nome()
    else:
        return idade


def valida_salario():
    salario = input('Digite o salário: R$ ')

    try:
        salario = float(salario)
    except ValueError:
        print('Digite um valor de salário válido.')
        print()
        valida_salario()

    if salario < 1:
        print('Digite um salário maior que 0.')
        print()
        valida_salario()
    else:
        salario = f'{salario:.2f}'
        salario = str(salario)
        salario = salario.replace('.', ',')
        return salario


def valida_sexo():
    sexo = input('Selecione o sexo [M] Masculino - [F] Feminino: ')

    try:
        sexo = sexo.upper()
    except ValueError:
        print('Escolha [M] para masculino ou [F] para feminino.')
        print()
        valida_sexo()

    if sexo != 'M' and sexo != 'F':
        print('Escolha [M] ou [F].')
        print()
        valida_sexo()
    else:
        if sexo == 'M':
            sexo = 'Masculino'
        if sexo == 'F':
            sexo = 'Feminino'
        return sexo


def valida_estado_civil():
    estado = input('[S] Solteiro(a)\n'
                   '[C] Casado(a)\n'
                   '[V] Viúvo(a)\n'
                   '[D] Divorciado(a)\n'
                   'Escolha o estado civil: ')
    print()
    estado = estado.upper()

    try:
        estado = estado.upper()
    except:
        print('Escolha uma opção válida.')
        valida_estado_civil()

    if estado != 'S' and estado != 'C' and estado != 'V' and estado != 'D':
        print('Digite uma opção válida.')
        valida_estado_civil()
    else:
        if estado == 'S':
            estado = 'Solteiro'
        if estado == 'C':
            estado = 'Casado'
        if estado == 'V':
            estado = 'Viúvo'
        if estado == 'D':
            estado = 'Divorciado'

    return estado


nome = valida_nome()
idade = valida_idade()
salario = valida_salario()
sexo = valida_sexo()
estado = valida_estado_civil()


print(f'Nome: {nome}\n'
      f'Idade: {idade}\n'
      f'Salário: R$ {salario}\n'
      f'Sexo: {sexo}\n'
      f'Estado civil: {estado}')
