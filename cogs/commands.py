from discord.ext import commands
import discord
from discord import app_commands
import os


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="commands", description="Shows all commands this bot has to offer")
    async def commands(self, interaction: discord.Interaction):
        
        def clean_filename(filename):
            return filename.replace(".py", "").replace("'", "").replace("[", "").replace("]", "").replace(",", "")

        def get_cog_filenames():
            cog_folder = "cogs"
            cog_filenames = [filename for filename in os.listdir(cog_folder) if filename.endswith(".py") and filename != "__init__.py"]
            clean_filenames = [clean_filename(filename) for filename in cog_filenames]
            return clean_filenames

        # Call the function to get the list of cleaned cog filenames
        cleaned_cog_filenames = get_cog_filenames()

        # Format the cleaned filenames with bullet points
        formatted_filenames = "\n".join([f"• {filename}" for filename in cleaned_cog_filenames])

        # Print the formatted list of filenames
        await interaction.response.send_message(formatted_filenames)

async def setup(bot):
    await bot.add_cog(Commands(bot))