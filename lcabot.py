import os
import discord
from oauthlib.oauth2 import WebApplicationClient

TOKEN = 'abcdefg.fake.token.1234567'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    response = 'hi friend'
    await message.channel.send(response)

client.run(TOKEN)

