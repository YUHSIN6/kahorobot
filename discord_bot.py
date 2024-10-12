import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
ID_admin = os.getenv("ID_6UC")

# 設置 Intents 和 Bot
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

# 允許使用命令的用戶ID
ALLOWED_USERS = [ID_admin]  # 替換為實際的 Discord 用戶 ID

# 限定特定指令的裝飾器
def is_allowed_user():
    async def predicate(ctx):
        return ctx.author.id in ALLOWED_USERS
    return commands.check(predicate)

# 自訂義的幫助命令類別
class CustomHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        ctx = self.context
        user = ctx.author
        
        # 用於顯示的embed
        embed = discord.Embed(title="Bot Commands", description="Here are the available commands:", color=discord.Color.blue())

        if user.id in ALLOWED_USERS:
            # 顯示所有指令
            for cog, commands in mapping.items():
                if cog:
                    cog_name = cog.qualified_name
                    command_list = [f"`{cmd.name}`: {cmd.help or 'No description'}" for cmd in commands if await cmd.can_run(ctx)]
                    if command_list:
                        embed.add_field(name=cog_name, value="\n".join(command_list), inline=False)
        else:
            # 顯示有限的指令，或者根據需要自定義
            for cog, commands in mapping.items():
                if cog:
                    cog_name = cog.qualified_name
                    command_list = [f"`{cmd.name}`: {cmd.help or 'No description'}" for cmd in commands if await cmd.can_run(ctx)]
                    if command_list:
                        # 只顯示基本命令或不顯示某些Cog
                        embed.add_field(name=cog_name, value="\n".join(command_list), inline=False)
        
        await ctx.send(embed=embed)

    async def send_command_help(self, command):
        ctx = self.context
        embed = discord.Embed(
            title=f"Command: {command.name}",
            description=command.help or "No description provided.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    async def send_cog_help(self, cog):
        ctx = self.context
        embed = discord.Embed(
            title=f"Cog: {cog.qualified_name}",
            description="Commands in this cog:",
            color=discord.Color.orange()
        )
        command_list = [f"`{cmd.name}`: {cmd.help or 'No description'}" for cmd in cog.get_commands() if await cmd.can_run(ctx)]
        if command_list:
            embed.add_field(name=cog.qualified_name, value="\n".join(command_list), inline=False)
        await ctx.send(embed=embed)

    async def send_error_message(self, error):
        await self.context.send(error)

# 設置自訂義幫助命令
bot.help_command = CustomHelpCommand()

# 一開始bot開機需載入全部程式檔案
async def load_extensions(bot):
    for root, dirs, files in os.walk("./cogs"):
        for filename in files:
            if filename.endswith(".py"):
                # 将文件路径转换为符合 Python 模块的格式
                relative_path = os.path.relpath(os.path.join(root, filename), ".")
                module_path = relative_path.replace(os.sep, ".")[:-3]
                
                # 加载扩展
                await bot.load_extension(module_path)
                print(f"Loaded extension: {module_path}")

# 當機器人完成啟動時
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")

# 確定執行此py檔才會執行
async def main():
    async with bot:
        await load_extensions(bot)
        await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
