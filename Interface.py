import Blackjack


class Interface:
    def __init__(self):
        print('***********************')
        print('Bem-vindo ao GL Cassino!!')
        print('***********************\n')
        self.jogadores = []
        self.criar_jogadores()

    def criar_jogadores(self):
        continuar = True
        while continuar:
            nome = input('Digite o nome do jogador: ')
            deposito = float(input('Digite o valor do depósito: '))

            self.jogadores.append([nome, deposito])

            resposta = input('Deseja adicionar outro jogador? (s/n): ')
            if resposta.lower() != 's':
                continuar = False

    def mostrar_jogadores(self):
        print('Jogadores registrados:')
        for jogador in self.jogadores:
            print(f'Nome: {jogador[0]}, Saldo: R${jogador[1]}')

    def escolher_jogo(self):
        print('Escola o Jogo: ')
        print('R - Roleta')
        print('B - Blackjack')
        print('Caso não deseje apostar, digite "S" para sair e seu saldo será devolvido.')
        jogo = input('Digite a opção desejada: ')
        if jogo.lower() == 'b':
            blackjack = Blackjack.Blackjack()
            blackjack.iniciar_jogo()


interface = Interface()
interface.mostrar_jogadores()
interface.escolher_jogo()
