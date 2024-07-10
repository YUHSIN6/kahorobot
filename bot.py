import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

# 取得环境设置
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if DISCORD_TOKEN is None:
    raise ValueError("DISCORD_TOKEN is not set in the .env file")

# intents
intents = discord.Intents.default()
intents.message_content = True  # 新增要求读取消息权限

# bot
bot = commands.Bot(command_prefix='!', intents=intents)

# 打印当前工作目录
print(f"Current working directory: {os.getcwd()}")

# 打印 cogs 文件夹中的文件
print("Files in cogs folder:")
for filename in os.listdir("./cogs"):
    print(filename)

async def load_extensions():
    # 加载 cog 文件
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded extension: {filename}")
            except Exception as e:
                print(f"Failed to load extension {filename}: {e}")

@bot.event
async def on_ready():
    print(f"「{bot.user}」已登入")
    print("注册的命令：")
    for command in bot.commands:
        print(command.name)

async def main():
    await load_extensions()
    await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
