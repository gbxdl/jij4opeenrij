"""Generate AI moves based on model"""

import numpy as np


class Ai:
    def __init__(self):
        self.model = (
            np.random.random(
                42,
            )
            * 2
            - 1
        )

    def make_ai_move(self, bord, on_move):
        moves = np.zeros((7,))

        for zet in range(7):
            for row in range(6):
                hoogte = 5 - row
                if bord[hoogte][zet] == 0:
                    bord[hoogte][zet] = on_move
                    moves[zet] = np.linalg.norm(
                        np.dot(self.model, np.matrix.flatten(bord))
                    )
                    bord[hoogte][zet] = 0
                    break
        return np.argmax(moves)
