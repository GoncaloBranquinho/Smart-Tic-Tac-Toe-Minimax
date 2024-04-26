class Node:
    def __init__(self, partida, jogada):
        # Initialize a node with the current game state and default values
        self.partida = partida
        self.jogada = jogada
        self.children = []  # List to store child nodes

    def create_children(self):
        # Create child nodes 
        for posicao in self.partida.posicoes_vazias:
            self.children.append(Node(self.partida, posicao))
            # Create a new child node representing the game state after making a move