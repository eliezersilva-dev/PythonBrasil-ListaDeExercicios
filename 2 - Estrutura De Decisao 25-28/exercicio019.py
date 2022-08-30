"""
Eliezer Silva
Exercício 19
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
dezenas e unidades do mesmo.
Observando os termos no plural, a colocação do "e" e da vírgula. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
1 = 1 unidade
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

"""

# Cabeçalho do Programa
print()
print('-'*10 + ' Vericador de Centenas, Dezenas e Unidades '+'-'*10)
print()

# Entrada do valor - input
numero = int(input('Digite um número entre 1 e 999: '))

# Separando centena, dezena e unidade
centena = int(numero / 100)
dezena = int((numero - (centena * 100)) / 10)
unidade = int(numero - (centena * 100 + dezena * 10))

# Configurando o plural
string_centena = 'centena'
string_dezena = 'dezena'
string_unidade = 'unidade'

if centena > 1:
    string_centena = 'centenas'
if dezena > 1:
    string_dezena = 'dezenas'
if unidade > 1:
    string_unidade = 'unidades'

# Configurando a saída
resultado = f'{numero} = '

if centena != 0:
    resultado += f'{centena} {string_centena}'
if dezena != 0:
    resultado += f' {dezena} {string_dezena}'
if unidade != 0:
    resultado += f' {unidade} {string_unidade}'

# Configurando a vírgula e o "e"
if resultado == f'{numero} = {centena} {string_centena} {dezena} {string_dezena} {unidade} {string_unidade}':
    resultado = f'{numero} = {centena} {string_centena}, {dezena} {string_dezena} e {unidade} {string_unidade}'
if resultado == f'{numero} = {centena} {string_centena} {dezena} {string_dezena}':
    resultado = f'{numero} = {centena} {string_centena} e {dezena} {string_dezena}'
if resultado == f'{numero} = {centena} {unidade} {string_unidade}':
    resultado = f'{numero} = {centena} {string_centena} e {unidade} {string_unidade}'
if resultado == f'{numero} = {dezena} {string_dezena} {unidade} {string_unidade}':
    resultado = f'{numero} = {dezena} {string_dezena} e {unidade} {string_unidade}'

# Saída final
print(resultado)

