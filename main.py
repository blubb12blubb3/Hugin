import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
import os
from config import TOKEN

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=None, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=discord.CustomActivity(name=f"Helping {len(bot.users)} Players on their Valheim Journey"))
    print(f"{bot.user} is ready but not synced yet")
    update_status.start()
    print(f"{bot.user} started activity update cycle")
    slashsync = await bot.tree.sync()
    print(f"{bot.user} synced {len(slashsync)} commands.")

async def load_extensions():
    async def load_cogs(dir):
        for filename in os.listdir(dir):
                if filename.endswith(".py") and filename != "__init__.py":
                    await bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Cogs loaded from {dir}")
    dir1 = "./Hugin/cogs"
    dir2 = "./cogs"
    if os.path.exists(dir1):
        await load_cogs(dir1)
    elif os.path.exists(dir2):
        await load_cogs(dir2)

@tasks.loop(seconds = 100)
async def update_status():
    await bot.change_presence(activity=discord.CustomActivity(name=f"Helping {len(bot.users)} Players on their Valheim Journey"))

async def main():
    async with bot:
        await load_extensions()
        await bot.start(token=TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
    