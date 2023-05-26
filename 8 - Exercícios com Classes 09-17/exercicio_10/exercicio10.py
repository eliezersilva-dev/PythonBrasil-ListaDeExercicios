"""
Eliezer Silva
Exercício 10
-------------
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
i. tipoCombustivel;
ii. valorLitro;
iii. quantidadeCombustivel.

b. Possua no mínimo esses métodos:
i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi
colocada no veículo;
ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago
pelo cliente;
iii. alterarValor( ) – altera o valor do litro do combustível;
iv. alterarCombustivel( ) – altera o tipo do combustível;
v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""

# usando pra rascunho
# area de testes - apagar


import turtle
import time

turtle.Screen()
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


# import turtle
#
#
# def draw_rectangle(width, height):
#     turtle.forward(width)
#     turtle.left(90)
#     turtle.forward(height)
#     turtle.left(90)
#     turtle.forward(width)
#     turtle.left(90)
#     turtle.forward(height)
#
#
# # Example usage:
# draw_rectangle(100, 50)
# turtle.done()


