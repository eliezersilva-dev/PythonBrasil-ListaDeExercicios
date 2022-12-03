"""
Eliezer Silva
Exercício 11
-------------
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""

print()

vetor_um = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
vetor_dois = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K']
vetor_tres = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k']

print(f'Vetor Um: {vetor_um[::1]}')
print(f'Vetor Dois: {vetor_dois[::1]}')
print(f'Vetor Três: {vetor_tres[::1]}')

vetor_quatro = vetor_um + vetor_dois + vetor_tres
vetor_quatro[::3] = vetor_um
vetor_quatro[1::3] = vetor_dois
vetor_quatro[2::3] = vetor_tres

print(vetor_quatro)

# :)
