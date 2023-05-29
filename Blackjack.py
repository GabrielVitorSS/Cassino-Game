import random


class Blackjack:

    def __init__(self):
        self.num_decks = 6
        self.cartas = ['A', '2', '3', '4', '5',
                       '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.mao_dealer = []

    def iniciar_jogo(self):
        print('***********************')
        print('Bem-vindo ao Blackjack!')
        print('***********************\n')

        num_jogadores = int(
            input('Quantos jogadores estão participando?'))
        self.distribuir_cartas(num_jogadores)

    def distribuir_cartas(self, num_jogadores):
        maos_jogadores = []
        for jogador in range(num_jogadores):
            mao = random.sample(self.cartas, 2)
            maos_jogadores.append(mao)
            print(f'Jogador {jogador + 1}: {mao}')

        self.mao_dealer = random.sample(self.cartas, 2)
        self.distribuir_cartas_dealer()
        self.jogar_rodada(maos_jogadores)
        self.jogar_rodada_dealer()
        self.resultado_maos(maos_jogadores)

    def distribuir_cartas_dealer(self):
        print(f'Dealer: [{self.mao_dealer[0]}, Carta oculta]')

    def jogar_rodada(self, maos_jogadores):
        for jogador, mao in enumerate(maos_jogadores):
            while True:
                possibilidade = input(
                    f'Jogador {jogador + 1}, suas cartas são: {jogador + 1}: {mao}, você deseja mais uma carta? (s/n): ')
                if possibilidade.lower() == 's':
                    carta = random.choice(self.cartas)
                    mao.append(carta)
                    print(f'Jogador {jogador + 1}: {mao}')
                    somatorio = self.calcular_somatorio(mao)
                    if somatorio > 21:
                        print(f'Jogador {jogador + 1} estourou!')
                        break
                    elif somatorio == 21:
                        print(f'Jogador {jogador + 1} fez Blackjack!')
                        break
                elif possibilidade.lower() == 'n':
                    break
                else:
                    print(
                        'Opção inválida! Digite "s" para mais uma carta ou "n" para parar.')

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

    def resultado_maos(self, maos_jogadores):
        for jogador, mao in enumerate(maos_jogadores):
            somatorio = self.calcular_somatorio(mao)
            if somatorio > 21:
                print(f'Jogador {jogador + 1} estourou!')
            elif somatorio == 21:
                print(f'Jogador {jogador + 1} fez Blackjack!')
            else:
                somatorio_dealer = self.calcular_somatorio(self.mao_dealer)
                if somatorio_dealer > 21:
                    print(f'Jogador {jogador + 1} ganhou!')
                elif somatorio_dealer == 21:
                    print(f'Jogador {jogador + 1} perdeu!')
                elif somatorio > somatorio_dealer:
                    print(f'Jogador {jogador + 1} ganhou!')
                elif somatorio < somatorio_dealer:
                    print(f'Jogador {jogador + 1} perdeu!')
                elif somatorio == somatorio_dealer:
                    print(f'Jogador {jogador + 1} empatou!')
                else:
                    print('Erro inesperado!')


jogo = Blackjack()

jogo.iniciar_jogo()
