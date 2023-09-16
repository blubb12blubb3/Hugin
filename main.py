import discord
from discord.ext import commands
import asyncio
import os
from tk import TOKEN

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=None, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("ENTER YOUR ACTIVITY HERE"))
    print(f"{bot.user} is ready but not synced yet")
    slashsync = await bot.tree.sync()
    print(f"{len(slashsync)} commands synced.")


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(token=TOKEN)

asyncio.run(main())
