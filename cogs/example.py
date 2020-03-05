from discord.ext import commands


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
        await ctx.send('Working :]')


def setup(bot):
    bot.add_cog(Example(bot))
