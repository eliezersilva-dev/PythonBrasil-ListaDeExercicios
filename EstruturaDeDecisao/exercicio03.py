"""
Eliezer Silva
Exercício 03
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
M - Masculino, Sexo Inválido.
"""

verificador = input('Informe o sexo do usuário [M/F]: ')
verificador = verificador.upper()
if verificador == 'F':
    print('F - Feminino')
elif verificador == 'M':
    print('M - Masculino')
else:
    print(f'O dígito {verificador} não é válido')
