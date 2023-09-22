from discord.ext import commands
import discord
from discord import app_commands

class Soundtrack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="soundtrack", description="Link to the Official Valheim Soundtrack")
    async def soundtrack(self, interaction: discord.Interaction):
        await interaction.response.send_message("This Command is still in development.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Soundtrack(bot))
