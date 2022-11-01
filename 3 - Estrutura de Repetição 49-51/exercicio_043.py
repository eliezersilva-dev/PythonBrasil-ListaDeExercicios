"""
Eliezer Silva
Exercício 43
-------------
O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

print()
print('-' * 20 + ' Cardápio Lanchonete ' + '-' * 20)
print()

print('Especificação   Código  Preço\n'
      'Cachorro Quente 100     R$ 1,20\n'
      'Bauru Simples   101     R$ 1,30\n'
      'Bauru com ovo   102     R$ 1,50\n'
      'Hambúrguer      103     R$ 1,20\n'
      'Cheeseburguer   104     R$ 1,30\n' 
      'Refrigerante    105     R$ 1,00')

print()

pedido = f''
preco_total = 0

continuar = True

while continuar:
    codigo = input('Informe o código do pedido ou \n'
                   'digite [sair] para finalizar.\n'
                   'Código: ')

    print()

    if codigo == '100':
        print('Cachorro quente - Preço R$ 1,20')
        qtda_100 = int(input('Informe a quantidade desejada: '))
        preco_100 = qtda_100 * 1.20
        preco_total += preco_100
        pedido_100 = f'{qtda_100} Cachorro(s) quente(s) - R$ {preco_100:.2f}\n'
        pedido += pedido_100
        print()

    elif codigo == '101':
        print('Bauru Simples - Preço R$ 1,30')
        qtda_101 = int(input('Informe a quantidade desejada: '))
        preco_101 = qtda_101 * 1.30
        preco_total += preco_101
        pedido_101 = f'{qtda_101} Bauru(s) Simples - R$ {preco_101:.2f}\n'
        pedido += pedido_101
        print()

    elif codigo == '102':
        print('Bauru com ovo - R$ 1,50')
        qtda_102 = int(input('Informe a quantidade desejada: '))
        preco_102 = qtda_102 * 1.50
        preco_total += preco_102
        pedido_102 = f'{qtda_102} Bauru(s) com ovo - R$ {preco_102:.2f}\n'
        pedido += pedido_102
        print()

    elif codigo == '103':
        print('Hambúrguer - R$ 1,20')
        qtda_103 = int(input('Informe a quantidade desejada: '))
        preco_103 = qtda_103 * 1.20
        preco_total += preco_103
        pedido_103 = f'{qtda_103} Hambúrguer(es) - R$ {preco_103:.2f}\n'
        pedido += pedido_103
        print()

    elif codigo == '104':
        print('Cheeseburguer - R$ 1,30')
        qtda_104 = int(input('Informe a quantidade desejada: '))
        preco_104 = qtda_104 * 1.30
        preco_total += preco_104
        pedido_104 = f'{qtda_104} Cheeseburguer(s) - R$ {preco_104:.2f}\n'
        pedido += pedido_104
        print()

    elif codigo == '105':
        print('Refrigerante - Preço R$ 1,00')
        qtda_105 = int(input('Informe a quantidade desejada: '))
        preco_105 = qtda_105 * 1.00
        preco_total += preco_105
        pedido_105 = f'{qtda_105} Refrigerante(s) - R$ {preco_105}\n'
        pedido += pedido_105
        print()

    elif codigo == 'sair':
        continuar = False

print(f'Pedido:\n'
      f'{pedido}\n'
      f'Preço total: R$ {preco_total:.2f}')
