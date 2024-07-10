import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="%", intents=intents)

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
async def Hello(ctx):
    await ctx.send("Hello, world!")
    await ctx.message.delete()

# 從環境變量中獲取 token
token = os.getenv('DISCORD_BOT_TOKEN')
bot.run(token)
