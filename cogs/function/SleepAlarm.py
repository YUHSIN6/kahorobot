import discord
from discord.ext import commands, tasks
import os

ID_6uc = os.getenv("ID_6UC")
Channel_6uc = os.getenv("CHANNEL_6UC")

class SleepAlarm(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.send_sleep_message.start()
        print("SleepAlarm Cog has been initialized and task started.")

    @tasks.loop(minutes=1)  
    async def send_sleep_message(self):
        await self.bot.wait_until_ready()
        now = discord.utils.utcnow()  
        #print(f"Current UTC time: {now.hour}:{now.minute}")  
        if now.hour == 18 and now.minute == 00:
            channel = self.bot.get_channel(int(Channel_6uc))
            if channel:
                user_id = int(ID_6uc)  
                user = self.bot.get_user(user_id)
                if user:
                    await channel.send(f"<@{user.id}> 該去睡覺了！")


    @send_sleep_message.before_loop
    async def before_send_sleep_message(self):
        await self.bot.wait_until_ready()

# 將 Cog 添加到 bot
async def setup(bot: commands.Bot):
    await bot.add_cog(SleepAlarm(bot))
