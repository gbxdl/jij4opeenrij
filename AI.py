"""Generate AI moves based on model"""

import numpy as np


class Ai:

    def __init__(self):
        self.model = np.random.random((7,6))

    def make_ai_move(self, bord, on_move):
        moves = np.zeros((7,))

        for zet in range(7):
            for hoogte in range(6):
                if bord[hoogte][zet] == 0:
                    bord[hoogte][zet] = on_move
                    moves[zet] = np.linalg.norm(np.matmul(self.model, bord))
                    bord[hoogte][zet] = 0
                    break
        return np.argmax(moves)
