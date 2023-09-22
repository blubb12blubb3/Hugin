from discord.ext import commands
import discord
from discord import app_commands

class Quest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="quest", description="Random quests for Valheim")
    async def quest(self, interaction: discord.Interaction):
        await interaction.response.send_message("This Command is still in development.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Quest(bot))
