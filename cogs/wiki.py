from discord.ext import commands
import discord
from discord import app_commands

class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="wiki", description="Search the Valheim Wiki")
    async def wiki(self, interaction: discord.Interaction):
        await interaction.response.send_message("This Command is still in development. \nIn the meantime you can search here: https://valheim.fandom.com/wiki/Valheim_Wiki", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Wiki(bot))
