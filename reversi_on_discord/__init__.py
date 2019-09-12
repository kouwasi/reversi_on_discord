from discord import Client

client = Client()

@client.event
async def on_ready():
    print('Ready!')

@client.event
async def on_message(message):
    pass
