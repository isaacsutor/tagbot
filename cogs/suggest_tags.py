import discord
from discord.ext import commands
from discord import app_commands

class suggest_tags(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name='suggest_tags', description='Send hello!')
    async def suggest_tags(self, interaction: discord.Interaction):
        await interaction.response.send_message(content='Hello!')

async def setup(client: commands.Bot) -> None:
    await client.add_cog(suggest_tags(client))
