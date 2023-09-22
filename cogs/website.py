from discord.ext import commands
import discord
from discord import app_commands

class Website(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="website", description="Link to the Official Valheim Website")
    async def website(self, interaction: discord.Interaction):
        await interaction.response.send_message("https://www.valheim.com/", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Website(bot))
