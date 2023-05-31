import Blackjack
import Double


class Interface:
    def __init__(self):
        print('*************************')
        print('Bem-vindo ao GL Cassino!!')
        print('*************************\n')
        self.jogadores = []
        self.criar_jogadores()

    def criar_jogadores(self):
        continuar = True
        while continuar:
            nome = input('\nDigite o nome do jogador: ')
            deposito = float(input('Digite o valor do depósito: '))

            self.jogadores.append([nome, deposito])

            resposta = input('\nDeseja adicionar outro jogador? (s/n): ')
            if resposta.lower() != 's':
                continuar = False

    def mostrar_jogadores(self):
        print('\n \n \nJogadores registrados:')
        for jogador in self.jogadores:
            print(f'Nome: {jogador[0]}, Saldo: R${jogador[1]}')

    def escolher_jogo(self):
        print('\nEscolha o Jogo: ')
        print('D - Double')
        print('B - Blackjack')
        print('Caso não deseje apostar, digite "S" para sair e seu saldo será devolvido.')
        jogo = input('Digite a opção desejada: ')
        if jogo.lower() == 'b':
            game = Blackjack.Blackjack()
            game.jogar(self.jogadores)
        if jogo.lower() == 'd':
            game = Double.Double()
            game.jogar(self.jogadores)



interface = Interface()
interface.mostrar_jogadores()
interface.escolher_jogo()
