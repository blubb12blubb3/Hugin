from discord.ext import commands
import discord
from discord import app_commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="info", description="Shows info about this bot")
    async def info(self, interaction: discord.Interaction):
        await interaction.response.send_message("I am still in development. I will help you on your Valheim Journey in the future. Join this Server for updates: https://discord.gg/DF6HRjzzRh")


async def setup(bot):
    await bot.add_cog(Info(bot))
