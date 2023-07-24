"""
Eliezer Silva
Exercício 06
-------------
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o
número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem
dentro de faixas válidas.
"""
print()


class Televisao:

    def __init__(self, ):
        self.ligada = False
        self.canal = 0
        self.volume = 0

    def ligar(self):
        self.ligada = True
        print('TV Ligada.')

    def mudar_canal(self):
        if self.ligada is False:
            print('TV desligada.')
        else:
            self.canal += 1
            print(f'Canal: {self.canal}')

    def aumentar_volume(self):
        if self.ligada is False:
            print('TV desligada')
        else:
            self.volume += 1
            print(f'Volume: {self.volume}')

    def diminuir_volume(self):
        if self.ligada is False:
            print('TV desligada')
        else:
            self.volume -= 1
            print(f'Volume: {self.volume}')

    def desligar(self):
        self.ligada = False
        print('TV desligada')


televisao = Televisao()
televisao.ligar()
televisao.mudar_canal()
televisao.mudar_canal()
televisao.aumentar_volume()
televisao.aumentar_volume()
televisao.diminuir_volume()
televisao.desligar()
