from discord.ext import commands
import discord
from discord import app_commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="info", description="Shows info about this bot")
    async def info(self, interaction: discord.Interaction):
        await interaction.response.send_message("This is a template. You can write anything you want here.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Info(bot))
