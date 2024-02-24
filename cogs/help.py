from discord.commands import slash_command
from discord.ext import commands
import discord.ext
import discord


class Help(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot
    
    
    @slash_command(description="Show Help ")
    async def help(self, ctx: discord.ApplicationContext, which=None):
                    
        if which is not None and which.lower() == "error":
            embed = discord.Embed(title="5Head - Help",
                      description="The `/error` Command - for Nintendo Errorcodes\n\nHow to get the Description of the Errorcode?\n> The command looks like this:\n```\n/error 0x27e\n```\n> The Output looks like this:\n\n```\n0x27e\nDescription: ResultInvalid\n```\n\n> Pls replace the `0x27e` with your Errorcode",
                      colour=0x00b0f4,
            )

            embed.set_footer(text="5Head",
                            icon_url="https://switchscene.org/attachments/1643075286239-png.1692/")

            await ctx.respond(embed=embed, ephemeral=True)
            
        else:
            embed = discord.Embed(title="5Head - Help",
                    description="The `/help` Command - its just a help command\n\n> Options for the `/help` Command\n```\n/help which: error\n```\n> New command coming soon, i think.",
                    colour=0x00b0f4
            )

            embed.set_footer(text="5Head",
                            icon_url="https://switchscene.org/attachments/1643075286239-png.1692/")

            await ctx.respond(embed=embed, ephemeral=True)
                    
        
def setup(bot: discord.Bot):
    bot.add_cog(Help(bot))