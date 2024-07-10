import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# 取得環境設定
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# 检查是否正确加载
if DISCORD_TOKEN is None:
    raise ValueError("DISCORD_TOKEN is not set in the .env file")

# intents
intents = discord.Intents.default()
intents.message_content = True  # 新增要求讀取訊息權限

# bot
bot = commands.Bot(command_prefix='!', intents=intents)

# 定义一个命令
@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world!")
    await ctx.message.delete()

# 事件处理器，检测关键字
@bot.event
async def on_message(message):
    # 防止机器人回复自己的消息
    if message.author == bot.user:
        return

    # 检查关键字
    if 'ping' in message.content:
        await message.channel.send('pong')

    # 确保命令处理正常工作
    await bot.process_commands(message)

# 事件处理器，机器人准备好时触发
@bot.event
async def on_ready():
    print(f"「{bot.user}」已登入")

# 启动机器人
bot.run(DISCORD_TOKEN)
