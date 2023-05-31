import random
import Interface


class Double:

    def init(self):
        self.numeros = [i for i in range(0,15)]
        self.corVermelho = [1, 2, 3, 4, 5, 6, 7]
        self.corPreto = [8, 9, 10, 11, 12, 13, 14]
        self.corBranco = [15]

    def iniciar_roleta(self):
        print('\n\n\n\n\n\n\n*********************')
        print('Bem vindo ao Double!')
        print('*********************\n')

        def valor_aposta(self):
            for jogador in range(self.jogadores):
                num_apostas = int(
                    input(f'{jogador + 1} Qual o valor da sua aposta? '))
        def aposta_cor(self):
            for jogador in range(self.jogadores):
                aposta_cor = input(
                    f'{jogador + 1} Qual a cor da sua aposta? ')
