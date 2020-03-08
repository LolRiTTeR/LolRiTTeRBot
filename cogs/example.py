from discord.ext import commands

import discord
import datetime


class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def example_check(ctx):
        return ctx.author.id in [1234, 7328]

    @commands.command(name='decorators', enabled=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.dm_only()
    @commands.has_permissions(manage_messages=True)
    @commands.has_guild_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    @commands.bot_has_guild_permissions(manage_messages=True)
    @commands.is_nsfw()
    @commands.is_owner()  # bot owner
    @commands.check(example_check)
    async def dont_use_this(self, ctx):
        pass

    @commands.command(name='test')
    @commands.guild_only()
    async def test(self, ctx):
        embed = discord.Embed(title="List of user statistics",
                              colour=discord.Colour(0xFF00FF), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(1583627162))

        embed.set_thumbnail(url="https://minotar.net/avatar/LolRiTTeR")
        embed.set_author(name="LolRiTTeR", url="https://discordapp.com",
                         icon_url="https://minotar.net/avatar/LolRiTTeR")
        embed.set_footer(text="footer text", icon_url="https://minotar.net/avatar/LolRiTTeR")

        embed.add_field(name="Status", value="InGame", inline=True)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Example(bot))
