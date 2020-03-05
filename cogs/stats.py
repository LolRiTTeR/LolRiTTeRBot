from discord.ext import commands
import discord


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stats')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def stats(self, ctx):
        e = discord.Embed(title="Title", description="Description", color=0xFF00FF)
        e.add_field(name="Field 1", value="Hello!", inline=False)
        e.set_footer(text="This is a cool footer")
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Stats(bot))
