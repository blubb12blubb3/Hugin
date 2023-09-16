from discord.ext import commands
import discord
from discord import app_commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check the ping of the bot")
    async def ping(self, interaction: discord.Interaction):
        try:
            await interaction.response.send_message(f'Pong! I needed {round (self.bot.latency * 1000)} ms to respond')
        except:
            await interaction.response.send_message(f'I am not available')

async def setup(bot):
    await bot.add_cog(Ping(bot))
