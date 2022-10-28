"""
Eliezer Silva
Exercício 31
------------
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui
uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar.
O programa deverá receber um número desconhecido de valores referentes aos preços das
mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra.
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente
forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa
deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o
exemplo abaixo:

Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...
"""
print()

produtos = {}
cont = 1
total = 0
dinheiro = 0
troco = 0


def notinha():
    print()
    print('Lojas Tabajara')

    for i, j in produtos.items():
        print(f'{i}: R$ {j:.2f}')

    print(f'Total: R$ {total:.2f}\n'
          f'Dinheiro: R$ {dinheiro:.2f}\n'
          f'Troco: R$ {troco:.2f}')


def pagamento():
    global dinheiro
    global troco
    dinheiro = float(input('Qual o valor em dinheiro: R$ '))
    troco = dinheiro - total
    if dinheiro < total:
        print('Dinheiro insuficiente.')
        pagamento()
    else:
        notinha()


def inserir_produto():
    global produtos
    global cont
    global total
    key = f'Produto {cont}'
    value = float(input(f'Valor produto {cont}: '))
    cont += 1

    if value == 0:
        total = sum(produtos.values())
        print(f'Total: R$ {total:.2f}')
        pagamento()

    else:
        produtos.update({key: value})
        inserir_produto()


inserir_produto()









