import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
import os
from tk import TOKEN

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=None, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=discord.CustomActivity(name=f"Helping {len(bot.users)} Players on their Valheim Journey"))
    print(f"{bot.user} is ready but not synced yet")
    update_status.start()
    slashsync = await bot.tree.sync()
    print(f"{len(slashsync)} commands synced.")

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            await bot.load_extension(f"cogs.{filename[:-3]}")

@tasks.loop(seconds = 100)
async def update_status():
    await bot.change_presence(activity=discord.CustomActivity(name=f"Helping {len(bot.users)} Players on their Valheim Journey"))

async def main():
    async with bot:
        await load_extensions()
        await bot.start(token=TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
    