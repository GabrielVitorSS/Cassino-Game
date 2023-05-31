import random


class Double:

    def __init__(self):
        self.numeros = [i for i in range(1,15)]
        self.corVermelho = [1, 2, 3, 4, 5, 6, 7]
        self.corPreto = [8, 9, 10, 11, 12, 13, 14]
        self.corBranco = [15]
        self.resultado = random.choice(self.numeros)

    def iniciar_roleta(self, jogadores):
        print('\n\n\n\n\n\n\n*********************')
        print('Bem vindo ao Double!')
        print('*********************\n')
        self.valor_aposta(jogadores)
        self.aposta_cor(jogadores)
        self.resultado_apostas(jogadores)

    def valor_aposta(self, jogadores):
         for jogador in jogadores:
            nome_jogadores = jogador[0]
            saldo = jogador[1]
            apostas = int(
                input(f'{nome_jogadores} Qual o valor da sua aposta? Seu saldo atual é de R${saldo} '))
            while apostas > saldo:
                print('Saldo insuficiente. Digite um valor válido.')
                apostas = int(
                    input(f'{nome_jogadores} Qual o valor da sua aposta? Seu saldo atual é de R${saldo} '))
                jogador.append(apostas)
    def aposta_cor(self, jogadores):
        for jogador in jogadores:
            nome_jogadores = jogador[0]
            print('As cores disponíveis são: Vermelho, Preto e Branco. A cor Vermelha e preta dobrará o valor apostado caso seja apostado nela, ja a Branca multiplicara o valor apostado por 14')
            aposta_cor = input(
                f'{nome_jogadores} Qual a cor da sua aposta? ')
            while aposta_cor.lower() != 'vermelho' and aposta_cor.lower() != 'preto' and aposta_cor.lower() != 'branco':
                print('Cor inválida. Digite uma cor válida.')
                aposta_cor = input(
                    f'{nome_jogadores} Qual a cor da sua aposta? ')     
    def resultado_apostas(self, jogadores):
         for jogador in jogadores:
            nome_jogadores = jogador[0]
            saldo = jogador[1]
            aposta = jogador[2]
            if self.resultado in self.corVermelho == 'vermelho':
                print(f'{nome_jogadores} Você ganhou R${aposta * 2}')
            if self.resultado in self.corPreto == 'preto':
                print(f'{nome_jogadores} Você ganhou R${aposta * 2}')
            if self.resultado in self.corBranco == 'branco':
                print(f'{nome_jogadores} Você ganhou R${aposta * 14}')

    def jogar(self, jogadores):
        self.iniciar_roleta(jogadores)