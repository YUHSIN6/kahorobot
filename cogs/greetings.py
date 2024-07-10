from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Greetings Cog initialized")  # 调试输出

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, world!")
        await ctx.message.delete()

def setup(bot):
    print("Loading Greetings Cog")  # 调试输出
    bot.add_cog(Greetings(bot))
