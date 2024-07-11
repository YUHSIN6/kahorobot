import discord
from discord.ext import commands

# 定義名為 Main 的 Cog
class Love(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 前綴指令
    @commands.command()
    async def love(self, ctx: commands.Context, *, content: str):
        await ctx.send("愛してるよ")



# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Love(bot))