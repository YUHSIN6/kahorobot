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

ALLOWED_USERS = [468711293264855052]  # 替換為實際的 Discord 用戶 ID

# 限定特定指令
def is_allowed_user():
    async def predicate(ctx):
        return ctx.author.id in ALLOWED_USERS
    return commands.check(predicate)
"""
# 自定义帮助命令
class CustomHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        ctx = self.context
        user = ctx.author
        allowed_cogs = []
        for cog, commands in mapping.items():
            if cog and any(await cmd.can_run(ctx) for cmd in commands):
                allowed_cogs.append(cog)
        if user.id in ALLOWED_USERS:
            await self.send_cogs_help(allowed_cogs)
        else:
            await self.send_error_message("You are not allowed to see this help message.")

    async def send_cogs_help(self, cogs):
        ctx = self.context
        embed = discord.Embed(title="Help", color=discord.Color.blue())
        for cog in cogs:
            commands = [cmd for cmd in cog.get_commands() if await cmd.can_run(ctx)]
            if commands:
                embed.add_field(name=cog.qualified_name, value="\n".join([cmd.name for cmd in commands]), inline=False)
        await ctx.send(embed=embed)

    async def send_error_message(self, error):
        await self.context.send(error)

bot.help_command = CustomHelpCommand()
"""
# 一開始bot開機需載入全部程式檔案
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded extension: {filename[:-3]}")

# 當機器人完成啟動時
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")

# 確定執行此py檔才會執行
async def main():
    async with bot:
        await load_extensions()
        await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
