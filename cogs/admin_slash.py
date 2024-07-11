import discord
from discord.ext import commands
from discord import app_commands

# 用于检查特定用户
def is_allowed_user():
    def predicate(interaction: discord.Interaction):
        allowed_users = [468711293264855052]  # 在这里填入允许使用命令的用户ID
        return interaction.user.id in allowed_users
    return app_commands.check(predicate)

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="load", description="Load a cog")
    @is_allowed_user()
    async def load(self, interaction: discord.Interaction, extension: str):
        await self.bot.load_extension(f"cogs.{extension}")
        await interaction.response.send_message(f"Loaded {extension} done.")

    @app_commands.command(name="unload", description="Unload a cog")
    @is_allowed_user()
    async def unload(self, interaction: discord.Interaction, extension: str):
        await self.bot.unload_extension(f"cogs.{extension}")
        await interaction.response.send_message(f"Unloaded {extension} done.")

    @app_commands.command(name="reload", description="Reload a cog")
    @is_allowed_user()
    async def reload(self, interaction: discord.Interaction, extension: str):
        await self.bot.reload_extension(f"cogs.{extension}")
        await interaction.response.send_message(f"Reloaded {extension} done.")

    @app_commands.command(name="shutdown", description="Shutdown the bot")
    @is_allowed_user()
    async def shutdown(self, interaction: discord.Interaction):
        await interaction.response.send_message("Shutting down...")
        await self.bot.close()

async def setup(bot):
    await bot.add_cog(AdminCommands(bot))
