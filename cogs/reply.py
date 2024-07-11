import discord
from discord.ext import commands

# 定義名為 Reply 的 Cog
class Reply(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 當有人標註機器人時回復原消息
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if self.bot.user.mentioned_in(message) and not message.mention_everyone and message.author != self.bot.user:
            await message.reply("？")
            #await message.channel.send(f"{message.author.mention} ？\n{message.content}")

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Reply(bot))
