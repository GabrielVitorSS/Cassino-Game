import random


class Blackjack:
    def __init__(self):
        self.num_decks = 6
        self.cartas = ['A', '2', '3', '4', '5',
                       '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.mao_dealer = []

    def iniciar_jogo(self, jogadores):
        print('\n\n\n\n\n\n\n***********************')
        print('Bem-vindo ao Blackjack!')
        print('***********************\n')
        self.fazer_apostas(jogadores)
        self.distribuir_cartas(jogadores)

    def fazer_apostas(self, jogadores):
        for jogador in jogadores:
            nome_jogador = jogador[0]
            saldo = jogador[1]
            aposta = float(input(f'Jogador {nome_jogador}, faça sua aposta (saldo disponível: R${saldo}): '))
            while aposta > saldo:
                print('Saldo insuficiente. Digite um valor válido.')
                aposta = float(input(f'Jogador {nome_jogador}, faça sua aposta (saldo disponível: R${saldo}): '))
            jogador.append(aposta)

    def distribuir_cartas(self, jogadores):
        maos_jogadores = []
        for jogador in jogadores:
            nome_jogador = jogador[0]
            mao = random.sample(self.cartas, 2)
            maos_jogadores.append([nome_jogador, mao])
            print(f'Jogador {nome_jogador}: {mao}')

        self.mao_dealer = random.sample(self.cartas, 2)
        self.distribuir_cartas_dealer()
        self.jogar_rodada(maos_jogadores)
        self.jogar_rodada_dealer()
        self.resultado_maos(maos_jogadores, jogadores)
        self.mostrar_saldos(jogadores)
        self.jogar_novamente(jogadores)

    def distribuir_cartas_dealer(self):
        print(f'Dealer: [{self.mao_dealer[0]}, Carta oculta]')

    def jogar_rodada(self, maos_jogadores):
        for mao in maos_jogadores:
            nome_jogador = mao[0]
            mao = mao[1]
            while True:
                possibilidade = input(f'Jogador {nome_jogador}, suas cartas são: {mao}, você deseja mais uma carta? (s/n): ')
                if possibilidade.lower() == 's':
                    carta = random.choice(self.cartas)
                    mao.append(carta)
                    print(f'Jogador {nome_jogador}: {mao}')
                    somatorio = self.calcular_somatorio(mao)
                    if somatorio > 21:
                        print(f'Jogador {nome_jogador} estourou!')
                        break
                    elif somatorio == 21:
                        print(f'Jogador {nome_jogador} fez Blackjack!')
                        break
                elif possibilidade.lower() == 'n':
                    break
                else:
                    print('Opção inválida! Digite "s" para mais uma carta ou "n" para parar.')

    def calcular_somatorio(self, mao):
        somatorio = 0
        as_count = 0
        for carta in mao:
            if carta.isdigit():
                somatorio += int(carta)
            elif carta in ['J', 'Q', 'K']:
                somatorio += 10
            elif carta == 'A':
                somatorio += 11
                as_count += 1

        while somatorio > 21 and as_count > 0:
            somatorio -= 10
            as_count -= 1

        return somatorio

    def jogar_rodada_dealer(self):
        print('\nDealer: ', self.mao_dealer)
        somatorio_dealer = self.calcular_somatorio(self.mao_dealer)

        while somatorio_dealer < 17:
            carta = random.choice(self.cartas)
            self.mao_dealer.append(carta)
            somatorio_dealer = self.calcular_somatorio(self.mao_dealer)
            print('Dealer recebeu uma carta: ', carta)
            print('Dealer: ', self.mao_dealer)
            print('Somatório do dealer é: ', somatorio_dealer)

    def resultado_maos(self, maos_jogadores, jogadores):
        for mao in maos_jogadores:
            nome_jogador = mao[0]
            mao = mao[1]
            somatorio = self.calcular_somatorio(mao)
            if somatorio > 21:
                print(f'Jogador {nome_jogador} estourou!')
                self.pagar_perdedor(nome_jogador, jogadores)
            elif somatorio == 21:
                print(f'Jogador {nome_jogador} fez Blackjack!')
                self.pagar_ganhador(nome_jogador, jogadores)
            else:
                somatorio_dealer = self.calcular_somatorio(self.mao_dealer)
                if somatorio_dealer > 21:
                    print(f'Jogador {nome_jogador} ganhou!')
                    self.pagar_ganhador(nome_jogador, jogadores)
                elif somatorio_dealer == 21:
                    print(f'Jogador {nome_jogador} perdeu!')
                    self.pagar_perdedor(nome_jogador, jogadores)
                elif somatorio > somatorio_dealer:
                    print(f'Jogador {nome_jogador} ganhou!')
                    self.pagar_ganhador(nome_jogador, jogadores)
                elif somatorio < somatorio_dealer:
                    print(f'Jogador {nome_jogador} perdeu!')
                    self.pagar_perdedor(nome_jogador, jogadores)
                elif somatorio == somatorio_dealer:
                    print(f'Jogador {nome_jogador} empatou!')
                    self.pagar_empate(nome_jogador, jogadores)
                else:
                    print('Erro inesperado!')

    def pagar_ganhador(self, nome_jogador, jogadores):
        for jogador in jogadores:
            if jogador[0] == nome_jogador:
                aposta = jogador[2]
                saldo_atual = jogador[1]
                saldo_atual += aposta * 2
                jogador[1] = saldo_atual
                print(f'Jogador {nome_jogador} ganhou {aposta * 2}!')

    def pagar_perdedor(self, nome_jogador, jogadores):
        for jogador in jogadores:
            if jogador[0] == nome_jogador:
                aposta = jogador[2]
                saldo_atual = jogador[1]
                saldo_atual -= aposta
                jogador[1] = saldo_atual
                print(f'Jogador {nome_jogador} perdeu {aposta}!')

    def pagar_empate(self, nome_jogador, jogadores):
        for jogador in jogadores:
            if jogador[0] == nome_jogador:
                aposta = jogador[2]
                saldo_atual = jogador[1]
                jogador[1] = saldo_atual
                print(f'Jogador {nome_jogador} empatou! A aposta foi devolvida.')

    def mostrar_saldos(self, jogadores):
        print('\nSaldo final:')
        for jogador in jogadores:
            nome_jogador = jogador[0]
            saldo = jogador[1]
            print(f'Jogador {nome_jogador}: R${saldo}')

    def jogar_novamente(self, jogadores):
        resposta = input('\nDeseja jogar novamente? (s/n): ')
        if resposta.lower() == 's':
            for jogador in jogadores:
                jogador[2] = 0  # Zera a aposta dos jogadores
            self.iniciar_jogo(jogadores)
        else:
            print('Obrigado por jogar!')

    def jogar(self, jogadores):
        self.iniciar_jogo(jogadores)

