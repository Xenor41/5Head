from discord.ext.commands import Context
from discord.ext import commands
import discord.ext
import discord
import os

intents = discord.Intents.all()
status = discord.Status.dnd
intents.members = True
discord.Activity()

TOKEN="INSERT_TOKEN_HERE"

bot = discord.Bot(
    intents=intents
)


@bot.event
async def on_ready():
    os.system("clear")
    print(f"[OK] {bot.user} is Online")
    
@bot.slash_command(name="hello")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond(f"Hi, {ctx.user.mention}", ephemeral=True)

if __name__ == "__main__":
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

    bot.run(TOKEN)
