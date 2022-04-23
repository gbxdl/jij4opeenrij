"""Handles gameplay"""

import numpy as np

from gui import Gui
from AI import Ai


class Gameplay:
    def __init__(self):
        self.on_move = None
        self.board = None
        self.gui = Gui()
        self.ai = Ai()
        self.reset()
        self.last_move = None

    def reset(self):
        self.on_move = 1
        self.board = np.array([[0] * 7] * 6)

    def run_game(self):

        self.gui.show_board(self.board)
        if self.on_move == 1:
            move = self.gui.take_move()
        else:
            move = self.ai.make_ai_move(self.board, self.on_move)

        if not self.is_legal_move(move):
            print("not a legal move")
            self.run_game()
            return

        move_row, move_column = self.make_move(move)

        if self.game_over(move_row, move_column):
            self.gui.show_board(self.board)
            print("Game over")
            return

        self.on_move *= -1
        self.run_game()

    def make_move(self, move):
        col = move
        for irow in range(6):
            row = 5 - irow
            if self.board[row][col] == 0:
                self.board[row][col] = self.on_move
                return row, col

    def is_legal_move(self, move):
        if 0 not in self.board[:, move]:
            return False
        return True

    def game_over(self, move_row, move_column) -> bool:
        """Check if there's a 4 in a rows based on last move."""
        # check down
        for hor_delta in [-1, 0, 1]:
            counter = 1
            for idown in range(1, 4):
                try:
                    if (
                        self.board[move_row + idown][move_column + hor_delta * idown]
                        == self.on_move
                    ):
                        counter += 1
                        if counter == 4:
                            return True
                    else:
                        break
                except IndexError:
                    break

        # check sideways
        counter = 0
        for icolumn in range(7):
            if self.board[move_row][icolumn] == self.on_move:
                counter += 1
                if counter == 4:
                    return True
            else:
                counter = 0

        return False


game = Gameplay()
game.run_game()
