import discord
from discord.ext import commands
from discord import app_commands

class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hi", description="Say hello to the bot")
    async def hi(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello, world!")
        print(self.bot.cogs)



async def setup(bot):
    await bot.add_cog(SlashCommands(bot))
