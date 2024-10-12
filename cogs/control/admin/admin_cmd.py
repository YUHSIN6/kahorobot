import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
ID_admin = os.getenv("ID_6UC")

ALLOWED_USERS = [int(ID_admin)]  # 在这里填入允许使用命令的用户ID

def is_allowed_user():
    async def predicate(ctx):
        print(f"Checking if user {ctx.author.id} is allowed")  # 打印当前用户 ID
        allowed = ctx.author.id in ALLOWED_USERS
        print(f"User {ctx.author.id} allowed: {allowed}")  # 打印检查结果
        return allowed

    return commands.check(predicate)

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"Allowed users: {ALLOWED_USERS}")
        print(f"Admin user ID loaded: {ID_admin}")  # 确保 ID_admin 正确加载

    @commands.command(name="load", description="Load a cog")
    @is_allowed_user()  # 确保这里是加括号
    async def load(self, ctx, extension: str):
        await self.bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded {extension} done.")

    @commands.command(name="unload", description="Unload a cog")
    @is_allowed_user()  # 确保这里是加括号
    async def unload(self, ctx, extension: str):
        await self.bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"Unloaded {extension} done.")

    @commands.command(name="reload", description="Reload a cog")
    @is_allowed_user()  # 确保这里是加括号
    async def reload(self, ctx, extension: str):
        await self.bot.reload_extension(f"cogs.{extension}")
        await ctx.send(f"Reloaded {extension} done.")

    @commands.command(name="shutdown", description="Shutdown the bot")
    @is_allowed_user()  # 确保这里是加括号
    async def shutdown(self, ctx):
        await ctx.send("Shutting down...")
        await self.bot.close()
        print("Shut down successfully")

async def setup(bot):
    await bot.add_cog(AdminCommands(bot))
