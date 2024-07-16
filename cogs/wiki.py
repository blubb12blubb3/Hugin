from discord.ext import commands
import discord
from discord import app_commands
import asyncio
import fandom

class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="wiki", description="Search the Valheim Fandom Wiki")
#Language Choice
    @app_commands.choices(language=[
        app_commands.Choice(name="Čeština", value="cs"),
        app_commands.Choice(name="Deutsch", value="de"),
        app_commands.Choice(name="Français", value="fr"),
        app_commands.Choice(name="Polski", value="pl"),
        app_commands.Choice(name="Português do Brasil", value="pt-br"),
        app_commands.Choice(name="Русский", value="ru"),
        app_commands.Choice(name="Українська", value="uk"),])


    async def wiki(self, interaction: discord.Interaction, search: str, language: app_commands.Choice[str] = 'en'):
        #Config
        wikiname = "Valheim"

        #set wiki
        fandomname = wikiname.lower().replace(" ","")
        fandom.set_wiki(fandomname)
        fandom.set_lang(language.value)

        results = 3
        
        try:
            #fandom search
            result_list = fandom.search(search, results = results)
            #names -> page titles (List)
            names = []
            #numbers -> page ids (List)
            numbers = []
            for i, (name, number) in enumerate(result_list, 1):
                names.append(name)
                numbers.append(number)
        except Exception as ee:
            print(ee)
        if not result_list:
            failEmbed=discord.Embed(title="No search results.", 
                                    description=f"There are **no** search results for **{search}** in the {wikiname} Wiki.", 
                                    color=0x2b2d31)
            failEmbed.add_field(name="Link to all articles", value=f"https://{fandomname}.fandom.com/wiki/Special:AllPages", inline=False)
            failEmbed.set_thumbnail(url=self.bot.user.avatar.url)
            await interaction.response.send_message(embed=failEmbed, ephemeral=True)


            await interaction.response.send_message(content=f'No search results were found for "**{search}**". Please try another search.')

        #search result formatting
        emoji_mapping = {
        1: '1️⃣',
        2: '2️⃣',
        3: '3️⃣',
        4: '4️⃣',
        5: '5️⃣',
        6: '6️⃣',
        7: '7️⃣',
        8: '8️⃣',
        9: '9️⃣',
        }
        search_results = "\n".join([f"{emoji_mapping.get(i + 1, '❌')} {name}\n" for i, name in enumerate(names)])
        #search results embed send
        resultsEmbed=discord.Embed(title=f'Search Results for "{search}"', 
                            description=f"{search_results}", 
                            color=0x2b2d31)
        await interaction.response.send_message(embed=resultsEmbed)

        #add reactions to search result embed
        msg = await interaction.original_response()
        if 1 <= results <= 10:
            for i in range(1, results + 1):
                number_emoji = f"{i}\uFE0F\u20E3"
                await msg.add_reaction(number_emoji)
        else:
            await msg.add_reaction('❌')
            
        #check reactions
        def check(reaction, user):
            return user == interaction.user and reaction.message.id == msg.id     
        try:
            reaction = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            emoji = reaction[0].emoji
            user_reaction = None
            for key, value in emoji_mapping.items():
                if emoji == value:
                    user_reaction = key
                    break
        except asyncio.TimeoutError:
            await interaction.followup.send(content=f"{interaction.user.mention} did not react in time.")
        #except Exception as e1:
            #print(e1)
        await msg.clear_reactions()

        #loading page information
        loadingIcon = "<a:loading:1161668117861249134> "
        loadingEmbed=discord.Embed(title="",
                            description=f"Loading page information {loadingIcon}",
                            color=0x2b2d31)
        await interaction.edit_original_response(embed=loadingEmbed)
        
        #send result
        try:
            page = fandom.page(pageid = numbers[user_reaction - 1])

            page_title = page.title.replace(' ', '_')
            base_url = f"https://{fandomname}.fandom.com/{language.value}/wiki/{page_title}#"
            
            input_list = page.sections
            hyper_list = [f"[{item}]({base_url}{item.replace(' ', '_')})" for item in input_list]
            hyperlinks = str(hyper_list).replace("'","")
            hyperlinks = hyperlinks[1:-1]

            contentEmbed=discord.Embed(title=f"{page.title}", 
                            url=f"{page.url}",
                            description=f"{page.summary}", 
                            color=0x2b2d31)
            contentEmbed.set_footer(text=f"{wikiname} Wiki")
            contentEmbed.set_image(url=f"{page.images[0]}")
            theLine = "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"
            contentEmbed.add_field(name=theLine, value="**Sections: **", inline=False)
            for link in hyper_list:
                contentEmbed.add_field(name="", value=link, inline=False)
            contentEmbed.add_field(name=theLine, value="", inline=False)
            
            await interaction.edit_original_response(embed=contentEmbed)
        except Exception as e:
            await interaction.delete_original_response()
            await interaction.followup.send(content=f"Error: \n{e} \nHere is the link: \n{base_url[:-1]}")

async def setup(bot):
    await bot.add_cog(Wiki(bot))
