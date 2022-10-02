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


def funcao():

    global produtos
    global cont
    global total
    key = f'Produto {cont}'
    value = float(input('Valor produto: '))
    cont += 1

    if value == 0:

        for i, j in produtos.items():
            print()
            print('Lojas Tabajara')
            print(f'{i}: R$ {j:.2f}')

        total = sum(produtos.values())
        print('Total: {total}')
        quit()

    else:
        produtos.update({key: value})
        funcao()


funcao()









