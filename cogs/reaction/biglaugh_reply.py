import random
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
target_server = os.getenv("Daigaku_server_ID")

class RandomReply(commands.Cog):
    def __init__(self, bot: commands.Bot, target_guild_id: int, target_word: str):
        self.bot = bot
        self.target_guild_id = target_guild_id
        self.target_word = target_word

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user or message.guild.id != self.target_guild_id:
            return


        if self.target_word in message.content:
            if random.random() < 1/3:
                await message.channel.send("真的")

async def setup(bot):
    target_guild_id = target_server
    target_word = "超好笑" 
    await bot.add_cog(RandomReply(bot, target_guild_id, target_word))
