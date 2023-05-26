"""
Eliezer Silva
Exercício 09 - Opcional
-----------------------
Exercício resolvido com outras funcionalidades.
Obs: Nesse exercício utilizei as classes criadas no exercício 09 e criei o menu onde o usuário poderá
criar os objetos que serão exibidos em um interface gráfica simples (turtle).
"""
# Bibliotecas usadas no exercício
import turtle
import time


# Parei aqui: a função 'apresentar_retangulo' não renderiza a janela turtle
# a função é chamada, printa antes e depois da sequência de comandos turtle
# mas o turtle não renderiza. Fora da função o bloco turtle funciona. Por que?
# Por que? Por que? Por que? Por que? Por que? Por que? Por que? Por que? Por que?
# Perdi umas duas horas tentando resolver essa porcaria. Desisto. Vou dormir...


# Esta função irá apresentar ao usuário o resultado em uma interface gráfica simples.
def apresentar_retangulo():
    print('OK chamou a função')
    caneta = turtle.Turtle()
    caneta.speed(1)
    caneta.shape('circle')
    caneta.hideturtle()
    caneta.pensize(5)
    caneta.penup()
    caneta.goto(-250, -250)

    x = 100
    y = 50

    caneta.pendown()
    caneta.forward(x)
    caneta.left(90)
    caneta.forward(y)
    caneta.left(90)
    caneta.forward(x)
    caneta.left(90)
    caneta.forward(y)
    caneta.left(90)

    caneta2 = turtle.Turtle()
    caneta2.pencolor('red')
    caneta2.left(90)
    caneta2.forward(50)

    time.sleep(3)
    turtle.bye()

    print('\nAQUI -> Apresentação GRAFICA de "mostrar_retangulo"')

    menu()


# elif _funcao == 'encontrar_centro':
#     print('\nAQUI -> Apresentação GRAFICA de mostrar_centro')
# elif _funcao == 'encontrar_posicao':
#     print('\nAQUI -> Apresentação GRAFICA de mostrar_ponto')


# Criando a Classe Retângulo
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def mostrar_retangulo(self):
        print(f'\nMostrar Retângulo:\n'
              f'Largura: {self.largura}\n'
              f'Altura: {self.altura}')
        apresentar_retangulo()  # Aqui chama a função de apresentação da interface gráfica


# Criando a Classe Ponto
class Ponto:
    def __init__(self, ponto_x, ponto_y):
        self.ponto_x = ponto_x
        self.ponto_y = ponto_y

    def mostrar_ponto(self):
        print(f'\nPonto\n'
              f'Ponto X posição: {self.ponto_x}\n'
              f'Ponto Y posição: {self.ponto_y}')
        menu()


# Função para encontrar o centro do retângulo
def encontrar_centro(_retangulo):
    largura = retangulo.largura
    altura = retangulo.altura
    x = f'{largura / 2 :.2f}'
    y = f'{altura / 2 :.2f}'
    apresentacao('encontrar_centro')  # Aqui chama a função de apresentação da interface gráfica
    print(f'\nPosição centro do Retângulo: x{x}, y{y}')
    menu()


# Função para encontrar as posições dos pontos no retângulo
def encontrar_posicao(_retangulo, _ponto):
    largura = retangulo.largura
    altura = retangulo.altura
    x = ponto.ponto_x
    y = ponto.ponto_y
    apresentacao('encontrar_posicao')  # Aqui chama a função de apresentação da interface gráfica
    print(f'\nPosições dos Pontos no Retângulo:\n'
          f'Retângulo\n'
          f'Largura: {largura}, Altura: {altura}\n'
          f'Ponto\n'
          f'Posição ponto: x{x:.2f}, y{y:.2f}')
    menu()


# A opção aqui se deu por criar um único objeto de cada classe. Eles serão armazenados em variáveis Globais
# estando acessíveis para todas as funções que os chamar.
retangulo = ''
ponto = ''


# Função que cria o objeto Retângulo
def criar_retangulo():
    global retangulo

    print('\nCrie ou edite um retângulo:\n'
          'Informe a Largura e a Altura (valor máximo = 500).')

    largura = input('Largura: ')
    if largura.isdigit():
        largura = float(largura)
        if largura > 500:  # Limitado a 500 para melhor apresentação na intarface gráfica
            largura = 500
    else:
        print('>>> Informe um valor numérico maior que zero.')
        print()
        criar_retangulo()

    altura = input('Altura: ')
    if altura.isdigit():
        altura = float(altura)
        if altura > 500:
            altura = 500  # Limitado a 500 para melhor apresentação na intarface gráfica
    else:
        print('>>> Informe um valor numérico maior que zero.')
        print()
        criar_retangulo()

    retangulo = Retangulo(largura, altura)
    menu()


# Função que cria o objeto Ponto
def criar_ponto():
    global ponto

    print('\nCrie ou edite um Ponto:\n'
          'Informe a posição x e a posição y (valor máximo = 500).')

    x = input('Posição x: ')
    try:
        x = float(x)
        if x < 0:
            print('\n>>> Informe um valor numérico maior que zero.')
            menu()
        elif x > 500:
            x = 500
    except ValueError as erro:
        print('\n>>> Informe um valor numérico maior que zero.')
        menu()

    y = input('Posição y: ')
    try:
        y = float(y)
        if y < 0:
            print('\n>>> Informe um valor numérico maior que zero.')
            menu()
        elif y > 500:
            y = 500
    except ValueError as erro:
        print('\n>>> Informe um valor numérico maior que zero.')
        menu()

    ponto = Ponto(x, y)
    menu()


# Função que exibe o menu da aplicação. Esta função apresenta um menu interativo ao usuário
# onde, através dele, poderá ser escolhido criar os objetos e/ou retornar resultados.
def menu():
    print('\n' + '-' * 13 + ' MENU ' + 12 * '-')
    print('Criar Retângulo             [1]\n'
          'Editar Retângulo            [2]\n'
          'Criar Ponto                 [3]\n'
          'Editar Ponto                [4]\n'
          'Mostrar Retângulo           [5]\n'
          'Mostrar Valores do Ponto    [6]\n'
          'Mostrar Centro do Retângulo [7]\n'
          'Mostrar Posições dos Pontos [8]\n'
          'Sair                        [9]')

    opcao = input('Opção: ')

    if opcao.isnumeric():
        opcao = int(opcao)
        if opcao <= 0 or opcao > 9:
            print('\n>>> Digite uma opção válida\n')
            menu()
        else:
            if opcao == 1 or opcao == 2:
                criar_retangulo()
            elif opcao == 3 or opcao == 4:
                criar_ponto()
            elif opcao == 5:
                if retangulo == '':
                    print('>>> Crie um Retângulo.')
                    menu()
                else:
                    retangulo.mostrar_retangulo()
            elif opcao == 6:
                if ponto == '':
                    print('>>> Crie um Ponto.')
                    menu()
                else:
                    ponto.mostrar_ponto()
            elif opcao == 7:
                if retangulo == '' or ponto == '':
                    print('>>> Crie um Retângulo e um Ponto.')
                    menu()
                else:
                    encontrar_centro(retangulo)
            elif opcao == 8:
                if retangulo == '' or ponto == '':
                    print('>>> Crie um Retângulo e um Ponto.')
                    menu()
                else:
                    encontrar_posicao(retangulo, ponto)
            elif opcao == 9:
                print('\n>>> Finalizando...')
                quit()
    else:
        print('\n>>> Digite uma opção válida\n')
        menu()


menu()
