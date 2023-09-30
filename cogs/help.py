from discord.ext import commands
import discord
from discord import app_commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Get a list of Commands you can use")
    async def help(self, interaction: discord.Interaction):
        embed=discord.Embed(title="A list of Commands you can use:", color=0x7289da)
        #Guide
        embed.add_field(name="Guide", value="""/wiki - Search about anything on the Valheim Wiki 
                        /help - Well, it does this...""", inline=False)
        #Entertainment
        embed.add_field(name="Entertainment", value="""/music - Links to music""", inline=False)
        #Official
        embed.add_field(name="Official Valheim Content", value="""/discord - Discord Server Invite
                        /website - Website
                        /soundtrack - Soundtrack
                        /news - Updates
                        /steam - Steam Page""", inline=False)
        
        embed.add_field(name="", value="[Bot Support Discord Server](https://discord.gg/DF6HRjzzRh)", inline=True)
        embed.add_field(name="", value="[Official Valheim Discord Server](https://discord.gg/valheim)", inline=True)

        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_footer(text=interaction.user,icon_url=interaction.user.avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Help(bot))
