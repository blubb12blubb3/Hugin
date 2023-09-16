from discord.ext import commands
import discord
from discord import app_commands


class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="poll", description="Add Reactions for Polls")
    async def poll(self, interaction: discord.Interaction, msg: str):

        #check for a link and extract the message id
        if "discord" in msg:
            message_link = msg
            # split the message link by slashes
            segments = msg.split("/")
            # get the last segment (which in this case is the message id)
            msg_id = segments[-1]
        else:
            msg_id = msg
            message_link = (f"https://discord.com/channels/{interaction.guild_id}/{interaction.channel_id}/{msg}")

        #adding reactions
        try:
            message = await self.bot.get_channel(interaction.channel_id).fetch_message(int(msg_id))
            await message.add_reaction('✅')
            await message.add_reaction('❎')
            #add more reactions here if you want 
            #for custom emojis write :emoji_name:emoji_id and for animated ones a:emoji_name:emoji_id
            await interaction.response.send_message(f"Command executed on message: {message_link}", ephemeral=True)
        except:
            await interaction.response.send_message(f"Command failed on message: {message_link}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Poll(bot))
