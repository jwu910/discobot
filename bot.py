
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to {guild.name}',
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$google.it hello'):
        await message.channel.send('Hello World!')

client.run(TOKEN)
