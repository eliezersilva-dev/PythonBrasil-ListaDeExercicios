"""
Eliezer Silva
Exercício 15
-------------
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
- Mostre a quantidade de valores que foram lidos;
- Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
- Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
- Calcule e mostre a soma dos valores;
- Calcule e mostre a média dos valores;
- Calcule e mostre a quantidade de valores acima da média calculada;
- Calcule e mostre a quantidade de valores abaixo de sete;
- Encerre o programa com uma mensagem;
"""

print()
print('-'*10+' Digite Valores '+10*'-')
print()

valores = []
print()


def resultado():
    print()
    print('-'*10+' Resultado '+10*'-')
    print()
    print(f'Quantidade de valores lidos: {len(valores)}')
    print()

    valores_str = str(valores)
    valores_str = valores_str.replace('[', '')
    valores_str = valores_str.replace(']', '')
    print(f'Valores em ordem: {valores_str}')
    print()

    valores_inverso = list(reversed(valores))
    print('Valores inverso um abaixo do outro:')
    for i in valores_inverso:
        print(i)
    print()

    print(f'A soma dos valores é: {sum(valores)}')
    print()

    media = sum(valores) / len(valores)
    print(f'A média dos valores é: {media:.2f}')
    print()

    acima_media = []
    for i in valores:
        if i > media:
            acima_media.append(i)
    acima_media = str(acima_media)
    acima_media = acima_media.replace('[', '')
    acima_media = acima_media.replace(']', '')
    print(f'Valores acima da média: {acima_media}')
    print()

    menores_sete = []
    for j in valores:
        if j < 7:
            menores_sete.append(j)
    menores_sete = str(menores_sete)
    menores_sete = menores_sete.replace('[', '')
    menores_sete = menores_sete.replace(']', '')
    print(f'Valores abaixo de sete: {menores_sete}')
    print()

    print('Mensagem de encerramento do programa\n'
          'Bye :)')


def adicionar_valores():
    valor = (input('Digite um valor ou [-1] para finalizar: '))
    if valor == '-1':
        resultado()
    elif not valor.isnumeric():
        print('Erro: Digite um valor numérico inteiro.')
        adicionar_valores()
    else:
        valor = int(valor)
        valores.append(valor)
        adicionar_valores()


adicionar_valores()
