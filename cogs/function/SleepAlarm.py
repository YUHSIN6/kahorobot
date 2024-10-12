import discord
from discord.ext import commands, tasks

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
            channel = self.bot.get_channel(960578682399903804)
            if channel:
                user_id = 468711293264855052  
                user = self.bot.get_user(user_id)
                if user:
                    await channel.send(f"<@{user.id}> 該去睡覺了！")


    @send_sleep_message.before_loop
    async def before_send_sleep_message(self):
        await self.bot.wait_until_ready()

# 將 Cog 添加到 bot
async def setup(bot: commands.Bot):
    await bot.add_cog(SleepAlarm(bot))
