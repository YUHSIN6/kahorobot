from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # 防止机器人回复自己的消息
        if message.author == self.bot.user:
            return

        # 检查关键字
        if "ping" in message.content:
            await message.channel.send("pong")

async def setup(bot):
    await bot.add_cog(Events(bot))
