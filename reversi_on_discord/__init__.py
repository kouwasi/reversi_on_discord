from copy import copy

import numpy as np
from discord import Client

from reversi_on_discord.enums import Piece

client = Client()


def _initial_board_generator():
    board = np.array([[Piece.NONE for i in range(8)] for j in range(8)])
    for i in range(3, 5):
        board[i][i] = Piece.WHITE

    board[3][4] = Piece.BLACK
    board[4][3] = Piece.BLACK

    return board


inital_board = _initial_board_generator()
current_board = copy(inital_board)


@client.event
async def on_ready():
    print('Ready!')


@client.event
async def on_message(message):
    if message.author == client.user and message.mention_everyone:
        return

    global current_board
    command = message.content.split(' ')

    if command[0] == '!bc':
        current_board = copy(inital_board)
        await message.channel.send('cleared, glhf!')
        return

    if command[0] == '!bw':
        current_board[int(command[1])][int(command[2])] = Piece.WHITE
        await send_current_board(message.channel)
        return

    if command[0] == '!bb':
        current_board[int(command[1])][int(command[2])] = Piece.BLACK
        await send_current_board(message.channel)
        return

    if client.user.mentioned_in(message):
        await send_current_board(message.channel)


async def send_current_board(channel):
    line = ''
    for row in current_board:
        line += ''.join(list(map(lambda x: x.value, row))) + '\n'

    await channel.send(line)
