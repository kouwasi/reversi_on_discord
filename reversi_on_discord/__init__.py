import numpy as np
from discord import Client

from reversi_on_discord import board
from reversi_on_discord.enums import Piece

client = Client()


@client.event
async def on_ready():
    print('Ready!')


@client.event
async def on_message(message):
    if message.author == client.user and message.mention_everyone:
        return

    command = message.content.split(' ')

    if command[0] == '!bc':
        board.clear_board()
        await message.channel.send('cleared, glhf!')
        return

    if command[0] == '!bw':
        x, y = board.parse_coordinate(command[1:2])
        board.place_piece(x=x, y=y, piece=Piece.WHITE)
        await send_current_board(message.channel)
        return

    if command[0] == '!bb':
        x, y = board.parse_coordinate(command[1:2])
        board.place_piece(x=x, y=y, piece=Piece.BLACK)
        await send_current_board(message.channel)
        return

    if client.user.mentioned_in(message):
        await send_current_board(message.channel)


async def send_current_board(channel):
    line = ''
    for row in board.current_board:
        line += ''.join(list(map(lambda x: x.value, row))) + '\n'

    await channel.send(line)
