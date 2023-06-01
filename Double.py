import random
import time

class Double:
    def __init__(self):
        self.numeros = [i for i in range(1, 15)]
        self.corVermelho = [1, 2, 3, 4, 5, 6, 7]
        self.corPreto = [8, 9, 10, 11, 12, 13, 14]
        self.corBranco = [15]
        self.resultado = random.choice(self.numeros)

    def iniciar_roleta(self, jogadores):
        print('\n\n\n\n\n\n\n*********************')
        print('Bem-vindo ao Double!')
        print('*********************\n')
        self.valor_aposta(jogadores)
        self.aposta_cor(jogadores)
        self.rodar_roleta()
        self.resultado_apostas(jogadores)
        self.pagar_ganhador(jogadores)
        self.jogar_novamente(jogadores)

    def valor_aposta(self, jogadores):
        for jogador in jogadores:
            nome_jogador = jogador[0]
            saldo = jogador[1]
            aposta = int(input(f'{nome_jogador}, qual o valor da sua aposta? Seu saldo atual é de R${saldo}: '))
            while aposta > saldo:
                print('Saldo insuficiente. Digite um valor válido.')
                aposta = int(input(f'{nome_jogador}, qual o valor da sua aposta? Seu saldo atual é de R${saldo}: '))
            jogador.append(aposta)

    def aposta_cor(self, jogadores):
        for jogador in jogadores:
            nome_jogador = jogador[0]
            print('\n\nAs cores disponíveis são: Vermelho, Preto e Branco. A cor Vermelha e preta dobrará o valor apostado caso seja apostado nela, já a Branca multiplicará o valor apostado por 14.')
            aposta_cor = input(f'{nome_jogador}, qual a cor da sua aposta? ')
            while aposta_cor.lower() != 'vermelho' and aposta_cor.lower() != 'preto' and aposta_cor.lower() != 'branco':
                print('Cor inválida. Digite uma cor válida.')
                aposta_cor = input(f'{nome_jogador}, qual a cor da sua aposta? ')
            jogador.append(aposta_cor.lower())

    def rodar_roleta(self):
        print('A roleta está rodando...')
        time.sleep(2)    
        print('A roleta está rodando...')
        time.sleep(2)
        print('Está quase lá...')
        time.sleep(1)
        print('\n\n\nA roleta parou!')
        if self.resultado in self.corVermelho:
            print('A cor sorteada foi: Vermelho')
        elif self.resultado in self.corPreto:
            print('A cor sorteada foi: Preto')
        else:
            print('A cor sorteada foi: Branco')

    def pagar_ganhador(self, jogadores):
        for jogador in jogadores:
            nome_jogador = jogador[0]
            saldo = jogador[1]
            aposta = jogador[2]
            cor_aposta = jogador[3]
            if self.resultado in self.corVermelho and cor_aposta == 'vermelho':
                valor_ganho = aposta * 2
                novo_saldo = saldo + valor_ganho
                jogador[1] = novo_saldo
                print(f'\n\n{nome_jogador}, você ganhou R${valor_ganho}! Seu novo saldo é de R${novo_saldo}.')
            elif self.resultado in self.corPreto and cor_aposta == 'preto':
                valor_ganho = aposta * 2
                novo_saldo = saldo + valor_ganho
                jogador[1] = novo_saldo
                print(f'\n\n{nome_jogador}, você ganhou R${valor_ganho}! Seu novo saldo é de R${novo_saldo}.')
            elif self.resultado in self.corBranco and cor_aposta == 'branco':
                valor_ganho = aposta * 14
                novo_saldo = saldo + valor_ganho
                jogador[1] = novo_saldo
                print(f'\n\n{nome_jogador}, você ganhou R${valor_ganho}! Seu novo saldo é de R${novo_saldo}.')
            else:
                novo_saldo = saldo - aposta
                jogador[1] = novo_saldo
                print(f'\n\n{nome_jogador}, você perdeu. Seu novo saldo é de R${novo_saldo}.')

    def resultado_apostas(self, jogadores):
        for jogador in jogadores:
            nome_jogador = jogador[0]
            saldo = jogador[1]
            aposta = jogador[2]
            cor_aposta = jogador[3]
            if self.resultado in self.corVermelho and cor_aposta == 'vermelho':
                valor_ganho = aposta * 2
                jogador.append(valor_ganho)
            elif self.resultado in self.corPreto and cor_aposta == 'preto':
                valor_ganho = aposta * 2
                jogador.append(valor_ganho)
            elif self.resultado in self.corBranco and cor_aposta == 'branco':
                valor_ganho = aposta * 14
                jogador.append(valor_ganho)

    def jogar_novamente(self, jogadores):
        resposta = input('\nDeseja jogar novamente? (s/n): ')
        if resposta.lower() == 's':
            self.resultado = random.choice(self.numeros)
            self.iniciar_roleta(jogadores)
        else:
            print('Obrigado por jogar!')

    def jogar(self, jogadores):
        self.iniciar_roleta(jogadores)