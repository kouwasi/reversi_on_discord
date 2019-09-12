import numpy as np
from discord import Client

from reversi_on_discord.enums import Piece

client = Client()
inital_board = _initial_board_generator()


@client.event
async def on_ready():
    print('Ready!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return


def _initial_board_generator():
    board = np.array([[None for i in range(8)] for j in range(8)])
    for i in range(3, 5):
        board[i][i] = Piece.WHITE

    board[3][4] = Piece.BLACK
    board[4][3] = Piece.BLACK

    return board
