"""
Eliezer Silva
Exercício 15
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""
print()
print('*' * 10 + ' Cálculo de Triângulo ' + '*' * 10)
print()

lado_a = float(input('Informe o valor de um lado do triângulo: '))
lado_b = float(input('Informe o valor de outro lado do triângulo: '))
lado_c = float(input('Informe o valor de outro lado do triângulo: '))
triangulo = ''

if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
    pass
else:
    print('Os valores informados não formam um triângulo.')
    quit()

if lado_a == lado_b == lado_c:
    triangulo = 'Equilátero'
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    triangulo = 'Isósceles'
elif lado_a != lado_b != lado_c:
    triangulo = 'Escaleno'

print(f'Os valores informados formam um triângulo {triangulo}.')
