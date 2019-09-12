from copy import copy

import numpy as np

from reversi_on_discord.enums import Piece

# TODO: 書いてね


def _initial_board_generator():
    board = np.array([[Piece.NONE for i in range(8)] for j in range(8)])
    for i in range(3, 5):
        board[i][i] = Piece.WHITE

    board[3][4] = Piece.BLACK
    board[4][3] = Piece.BLACK

    return board


inital_board = _initial_board_generator()
current_board = copy(inital_board)


def clear_board():
    global current_board
    current_board = copy(inital_board)


def place_piece(x, y, piece):
    global current_board
    current_board[x][y] = piece


def parse_coordinate(command):
    x = None
    y = None
    return (1, 'b')
