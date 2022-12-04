"""
Eliezer Silva
Exercício 22
-------------
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de
fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de
200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode
aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber
um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza;
necessita troca do cabo ou conector;
quebrado ou inutilizado;
Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""

print()
mouse_identificacao = 1
mouses_defeitos = {}
necessita_esfera = 0
necessita_limpeza = 0
necessita_troca_cabo_conector = 0
quebrado_inutilizado = 0

print('Informe o código defeito:\n'
      '1 - Necessita da esfera\n'
      '2 - Necessita de limpeza\n'
      '3 - Necessita troca do cabo ou conector\n'
      '4 - Quebrado ou inutilizado')
print()


def finalizar():
    global necessita_esfera
    global necessita_limpeza
    global necessita_troca_cabo_conector
    global quebrado_inutilizado

    for i, j in mouses_defeitos.items():
        if j == 1:
            necessita_esfera += 1
        elif j == 2:
            necessita_limpeza += 1
        elif j == 3:
            necessita_troca_cabo_conector += 1
        elif j == 4:
            quebrado_inutilizado += 1

    print()
    print(f'Quantidade de mouses: {len(mouses_defeitos)}')
    print('Situação - Quantidade - Percentual')
    print(f'1 - Necessita de esfera {necessita_esfera} {(necessita_esfera*100)/len(mouses_defeitos):.2f}%')
    print(f'2 - Necessita de limpeza {necessita_limpeza} {(necessita_limpeza*100)/len(mouses_defeitos):.2f}%')
    print(f'3 - Necessita troca do cabo ou conector {necessita_troca_cabo_conector}'
          f' {(necessita_troca_cabo_conector*100)/len(mouses_defeitos):.2f}%')
    print(f'4 - Quebrado ou inutilizado {quebrado_inutilizado} {(quebrado_inutilizado*100)/len(mouses_defeitos):.2f}%')


def inserir_defeitos():
    global mouse_identificacao
    defeito = int(input(f'Informe o Defeito do mouse {mouse_identificacao}\n'
                        f'[1, 2, 3, 4] ou [0] para finalizar: '))
    if defeito != 1 and defeito != 2 and defeito != 3 and defeito != 4 and defeito != 0:
        print()
        print('Informe um valor válido.')
        print()
        inserir_defeitos()
    elif defeito == 0:
        finalizar()
    else:
        mouses_defeitos.update({f'{mouse_identificacao}': defeito})
        mouse_identificacao += 1
        inserir_defeitos()


inserir_defeitos()
