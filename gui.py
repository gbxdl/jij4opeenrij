"""Show bord and gather user import. Websiteje."""
import numpy as np


class Gui:
    def __init__(self):
        pass

    def show_board(self, board):
        for row in range(6):
            for col in range(7):
                if board[row][col] == -1:
                    board[row][col] = 2
        for file in range(6):
            print(board[file])

    def take_move(self):
        """Let user input numers 1-7"""
        try:
            move = int(input()) - 1
        except ValueError:
            print("Doe beter je best")
            move = self.take_move()
        if move < 0 or move > 6:
            print("please move between 1-7")
            move = self.take_move()

        return move
