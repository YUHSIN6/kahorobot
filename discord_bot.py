import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)


async def load_extensions(bot):
    for root, dirs, files in os.walk("./cogs"):
        for filename in files:
            if filename.endswith(".py"):

                relative_path = os.path.relpath(os.path.join(root, filename), ".")
                module_path = relative_path.replace(os.sep, ".")[:-3]
                
                try:
                    await bot.load_extension(module_path)
                    print(f"Loaded extension: {module_path}")
                except Exception as e:
                    print(f"Failed to load extension {module_path}. Error: {e}")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")


async def main():
    async with bot:
        await load_extensions(bot)
        await bot.start(DISCORD_TOKEN)
    

if __name__ == "__main__":
    asyncio.run(main())
