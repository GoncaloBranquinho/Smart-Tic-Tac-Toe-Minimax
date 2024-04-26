from nodes import Node
from minimax import MiniMax

class Jogo:
    def __init__(self, dimensao):
        # Initialize the game with the specified board dimension
        self.dimensao = dimensao
        self.tabuleiro = []
        self.posicoes_vazias = {}
        # Initialize the game board and empty positions
        for i in range(self.dimensao):
            self.tabuleiro.append([])
            for j in range(self.dimensao):
                self.tabuleiro[i].append('_')
                self.posicoes_vazias[(i, j)] = 1
        # Initialize lists to track row, column, and diagonal sums
        self.linhas = [0 for _ in range(self.dimensao)]
        self.colunas = [0 for _ in range(self.dimensao)]
        self.diagonais = [0, 0]
        # Define a dictionary to convert player symbols to numerical values
        self.converter = {'X': 1, 'O': -1, 1: 'X', 0: 'O'}
        self.n_jogada = 0
        self.jogador = 1
        # Define point values for winning configurations
        self.pontos = {}
        for i in range(-self.dimensao, self.dimensao + 1):
            self.pontos[i] = self.sinal(i)*(4**(abs(i)))
        self.pontos[0] = 0
        self.mostrar()
        # Start the game loop
        self.jogar()

    def sinal(self, x):
        if (x > 0):
            return 1
        elif (x < 0):
            return -1
        else:
            return 0

    def contar_pontos(self):
        pontuacao = 0
        for i in self.linhas:
            pontuacao += self.pontos[i]
        for i in self.colunas:
            pontuacao += self.pontos[i]
        for i in self.diagonais:
            pontuacao += self.pontos[i]
        return pontuacao

    def mostrar(self):
        for l in self.tabuleiro:
            print("|".join(l))

    def incrementar(self, x, y):
        # Place a player symbol on the specified position and update game state
        self.tabuleiro[y][x] = self.converter[self.jogador]
        self.posicoes_vazias.pop((y, x), None)
        self.diagonais[0] += self.converter[self.tabuleiro[y][x]]*(y == x)
        self.diagonais[1] += self.converter[self.tabuleiro[y][x]]*(y + x == self.dimensao - 1)
        self.linhas[y] += self.converter[self.tabuleiro[y][x]]
        self.colunas[x] += self.converter[self.tabuleiro[y][x]]

    def decrementar(self, x, y):
        # Remove a player symbol from the specified position and update game state
        self.posicoes_vazias[(y, x)] = 1
        self.diagonais[0] -= self.converter[self.tabuleiro[y][x]]*(y == x)
        self.diagonais[1] -= self.converter[self.tabuleiro[y][x]]*(y + x == self.dimensao - 1)
        self.linhas[y] -= self.converter[self.tabuleiro[y][x]]
        self.colunas[x] -= self.converter[self.tabuleiro[y][x]]
        self.tabuleiro[y][x] = '_'

    def verificar(self, x, y):
        # Check if the current move results in a win
        resultado = {1: "Jogador 1 vence!", 0: "Jogador 2 vence!"}
        if (abs(self.diagonais[0]) == self.dimensao or abs(self.diagonais[1]) == self.dimensao or abs(self.linhas[y]) == self.dimensao or abs(self.colunas[x]) == self.dimensao):
            print(resultado[self.jogador])
            return 1
        return 0
    
    def verificar_minimax(self, x, y):
        # Check if the current move results in a win (for minimax)
        if (abs(self.diagonais[0]) == self.dimensao or abs(self.diagonais[1]) == self.dimensao or abs(self.linhas[y]) == self.dimensao or abs(self.colunas[x]) == self.dimensao):
            return 1
        return 0

    def jogar(self):
        # Main game loop
        if (self.jogador == 0):
            # Player's turn
            y, x = map(int, input().split())
        else:
            # AI's turn (minimax algorithm)
            temp = self.jogada_minimax()
            x = temp.jogada[1]
            y = temp.jogada[0]
            print(y, x)
        self.incrementar(x, y)
        self.mostrar()
        if (self.verificar(x, y)):
            return 0
        self.n_jogada += 1
        self.jogador = not self.jogador
        if (self.n_jogada < self.dimensao**2):
            self.jogar()
        else:
            print("Empate!")
            return 0

    def jogada_minimax(self):
        head = Node(self, (-1, -1))
        AI = MiniMax(self, -self.converter[self.converter[self.jogador]])
        return AI.init_search(head, 3)


partida = Jogo(3)