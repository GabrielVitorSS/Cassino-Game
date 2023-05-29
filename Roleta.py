import random
import Interface


class Roleta:

    def __init__(self):
        self.numeros
        self.cor = ['vermelho', 'preto', 'verde']
        self.par_impar = ['par', 'impar']
        self.alto_baixo = ['alto', 'baixo']

    def iniciar_roleta(self):
        print('*******************')
        print('Bem vindo a Roleta!')
        print('*******************\n')

        def quantidade_apostas(self):
            for jogador in range(self.jogadores):
                num_apostas = int(
                    input(f'{jogador + 1} quantas apostas deseja fazer? '))
