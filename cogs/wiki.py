from discord.ext import commands
import discord
from discord import app_commands
import requests

class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="wiki", description="Search the Valheim Wiki")
    
    async def wiki(self, interaction: discord.Interaction, search: str, page_anchor: str = None):
    #search formatting
        unformatted_search = search
        search = search.replace(" ", "_")

        search_text = "There is currently no text in this page. You can search for this page title in other pages, or search the related logs, but you do not have permission to create this page."

    #Check for Page Anchor
        if page_anchor == None:
            url = f"https://valheim.fandom.com/wiki/{search}"
            combined_search = search
        elif page_anchor != None:
        #page anchor formatting
            unformatted_page_anchor = page_anchor
            page_anchor = page_anchor.replace(" ", "_")

            combined_search = f"{search}#{page_anchor}"
            url = f"https://valheim.fandom.com/wiki/{combined_search}"
    
    #Check if Article exists
        response = requests.get(url)
        if response.status_code == 200:
            page_content = response.text
            if search_text in page_content:
                await interaction.response.send_message(f"If you read this, you are either reading the source code or something is very broken (Code: wiki01)")
            else:
                await interaction.response.send_message(url)
    #That Article Doesn't Exist
        else:
            embed=discord.Embed(title="That Article Doesn't Exist.", 
                                description=f"There is **no** wiki article on **{search}**. Make sure you have spelled everything correctly. Sometimes the wiki can be a bit weird when it comes to capitalization. E.g: Ancient Tree and Ancient bark. You can manually search through all articles below.", 
                                color=0xc69c6d)
            embed.add_field(name="search", value=f"{unformatted_search}", inline=True)
            if page_anchor != None:
                embed.add_field(name="page_anchor", value=f"{unformatted_page_anchor}", inline=True)
            elif page_anchor == None:
                embed.add_field(name="page_anchor", value="-", inline=True)
            embed.add_field(name="Link to all articles", value="https://valheim.fandom.com/wiki/Special:AllPages", inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Wiki(bot))
