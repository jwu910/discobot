
import os
import sys

import discord
from discord import app_commands, ui
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

TARGET_CHANNEL="1061716765740109834"

"""
https://discordpy.readthedocs.io/en/latest/interactions/api.html?highlight=app+commands#modal
"""
class Client(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id=GUILD))
            self.synced = True
        print(
            f'{client.user} is connected to {self.user}',
        )

class TestModal(ui.Modal, title="Announcement"):
    content = ui.TextInput(label="Content", style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your response, title is {self.title}!', ephemeral=True)

client = Client()
tree = app_commands.CommandTree(client)

@tree.command(guild = discord.Object(id=GUILD), name="josh-test", description="Test description")
async def slash123(interaction: discord.Interaction):
    await interaction.response.send_message(f"This is working", ephemeral = True)

@tree.command(guild = discord.Object(id=GUILD), name="modal", description="Test description")
async def modalTest(interaction: discord.Interaction):
    modal = TestModal()
    await interaction.response.send_modal(modal)
    # await interaction.response.send_message(modal)



client.run(TOKEN)
