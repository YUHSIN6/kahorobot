import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)


ALLOWED_USERS = [468711293264855052]  # 替換為實際的 Discord 用戶 ID

def is_allowed_user():
    async def predicate(ctx):
        return ctx.author.id in ALLOWED_USERS
    return commands.check(predicate)


# 當機器人完成啟動時
@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

# 載入指令程式檔案
@bot.command()
@is_allowed_user()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} done.")

# 卸載指令檔案
@bot.command()
@is_allowed_user()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"UnLoaded {extension} done.")

# 重新載入程式檔案
@bot.command()
@is_allowed_user()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"ReLoaded {extension} done.")


#get user id
@bot.command()
async def get_id(ctx, member: discord.Member):
    await ctx.send(f"{member.name}'s ID is {member.id}")

# 一開始bot開機需載入全部程式檔案
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded extension: {filename[:-3]}")



async def main():
    async with bot:
        await load_extensions()
        # 使用 DISCORD_TOKEN 來啟動 bot
        await bot.start(DISCORD_TOKEN)

# 確定執行此py檔才會執行
if __name__ == "__main__":
    asyncio.run(main())