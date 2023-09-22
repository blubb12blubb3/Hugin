from discord.ext import commands
import discord
from discord import app_commands

class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="news", description="Link to the Valheim News Page on Steam")
    async def news(self, interaction: discord.Interaction):
        await interaction.response.send_message("This Command is still in development.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(News(bot))
