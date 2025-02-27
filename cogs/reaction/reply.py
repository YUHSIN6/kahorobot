import discord
from discord.ext import commands
import os

ID_admin = os.getenv("ID_6UC")
# 定義名為 Reply 的 Cog
class Reply(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.special_user_ids = [int(ID_admin)]

    # 當有人標註機器人時回復原消息
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if self.bot.user.mentioned_in(message) and not message.mention_everyone and message.author != self.bot.user:
            if message.author.id in self.special_user_ids:
                await message.reply("怎麼了")
            else:
                await message.reply("?")
            #await message.channel.send(f"{message.author.mention} ？\n{message.content}")

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Reply(bot))
