
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(
        f'{client.user} is connected to {guild.name}',
    )

    client.channels.get('the-after-hours').send('https://www.powerlanguage.co.uk/wordle/')

client.run(TOKEN)
