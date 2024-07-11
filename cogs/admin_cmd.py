import discord
from discord.ext import commands

ALLOWED_USERS = [468711293264855052]  # 在这里填入允许使用命令的用户ID

def is_allowed_user():
    async def predicate(ctx):
        return ctx.author.id in ALLOWED_USERS
    return commands.check(predicate)

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="load", description="Load a cog")
    @is_allowed_user()
    async def load(self, ctx, extension: str):
        await self.bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded {extension} done.")

    @commands.command(name="unload", description="Unload a cog")
    @is_allowed_user()
    async def unload(self, ctx, extension: str):
        await self.bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"Unloaded {extension} done.")

    @commands.command(name="reload", description="Reload a cog")
    @is_allowed_user()
    async def reload(self, ctx, extension: str):
        await self.bot.reload_extension(f"cogs.{extension}")
        await ctx.send(f"Reloaded {extension} done.")

    @commands.command(name="shutdown", description="Shutdown the bot")
    @is_allowed_user()
    async def shutdown(self, ctx):
        await ctx.send("Shutting down...")
        await self.bot.close()
        print("Shut down successfully")

async def setup(bot):
    await bot.add_cog(AdminCommands(bot))
