import discord
from discord.ext import commands
import os

class LineMessage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 将消息发送到 Discord 频道
    async def send_message_to_discord(self, message: str):
        print("a")
        channel = self.bot.get_channel(int(os.getenv("DISCORD_CHANNEL_ID")))  # 获取 Discord 频道
        if channel:
            await channel.send(message)

    # 处理接收到的消息并发送到 Discord
    @commands.Cog.listener()
    async def on_line_message(self, message: str):
        await self.send_message_to_discord(message)

    # 示例命令，用于手动测试发送消息到 Discord
    @commands.command(name='send')
    async def send(self, ctx, *, content: str):
        await self.send_message_to_discord(content)
        await ctx.send(f"消息已发送到 Discord 频道：{content}")

# 将 setup 函数定义为异步
async def setup(bot: commands.Bot):
    await bot.add_cog(LineMessage(bot))
