from discord.ext import commands
import discord
from discord import app_commands


class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="embed", description="ENTER COMMAND DESCRIPTION HERE")
    async def embed(self, interaction: discord.Interaction):

        embed=discord.Embed(title="Embed Title", description="Embed Description", color=0xc59d6d)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        #Field 1
        embed.add_field(name="Field 1 Title", value="Field 1 Description", inline=False)
        #Field 2
        embed.add_field(name="Field 2 Title", value="Field 2 Description", inline=False)
        #inline=False -> Field are under another, inline=True -> Fields are next to each other

        await interaction.response.send_message(embed=embed, ephemeral=True)
        #ephemeral=False -> everyone can see the bot response
        #ephemeral=True -> only command user can see bot response

async def setup(bot):
    await bot.add_cog(Embed(bot))
