import discord
from discord.ext import commands

# 定義名為 Main 的 Cog
class Echo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 前綴指令
    @commands.command()
    async def echo(self, ctx: commands.Context, *, content: str):
        await ctx.message.delete()
        await ctx.send(content)

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Echo(bot))
