import math

class MiniMax:
    def __init__(self, partida, original):
        # Initialize MiniMax with the current game state and player
        self.partida = partida
        self.original = original

    def init_search(self, node, depth):
        # Initialize the search for the best move using minimax algorithm
        node.create_children()
        greatest = math.inf
        for child in node.children:
            # Evaluate each child node and choose the best one
            self.partida.incrementar(child.jogada[1], child.jogada[0])
            self.partida.jogador = not self.partida.jogador
            value = self.deepen_search(child, depth - 1, True)
            self.partida.jogador = not self.partida.jogador
            self.partida.decrementar(child.jogada[1], child.jogada[0])
            if (value < greatest):
                greatest = value
                choice = child
        return choice

    def deepen_search(self, node, depth, is_maximizing):
        # Recursive function to explore the tree and evaluate positions
        if (depth == 0 or len(self.partida.posicoes_vazias) == 0 or self.partida.verificar_minimax(node.jogada[1], node.jogada[0]) == 1):
            # Base case
            return self.partida.contar_pontos() * self.original

        node.create_children()
        if (is_maximizing):
            # Maximizing player's turn
            greatest = -math.inf
            for child in node.children:
                self.partida.incrementar(child.jogada[1], child.jogada[0])
                self.partida.jogador = not self.partida.jogador
                greatest = max(greatest, self.deepen_search(child, depth - 1, False))
                self.partida.jogador = not self.partida.jogador
                self.partida.decrementar(child.jogada[1], child.jogada[0])
            return greatest
        else:
            # Minimizing player's turn
            smallest = math.inf
            for child in node.children:
                self.partida.incrementar(child.jogada[1], child.jogada[0])
                self.partida.jogador = not self.partida.jogador
                smallest = min(smallest, self.deepen_search(child, depth - 1, True))
                self.partida.jogador = not self.partida.jogador
                self.partida.decrementar(child.jogada[1], child.jogada[0])
            return smallest