from discord.ext import commands


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='reload')
    @commands.is_owner()
    async def _reload(self, ctx, *, module):
        try:
            self.bot.reload_extension(f'cogs.{module}')
        except commands.ExtensionError as e:
            await ctx.send(f'{e.__class__.__name__}: {e}')
        else:
            await ctx.send(f'Reloaded cog: {module}')

    @commands.command(name='load')
    @commands.is_owner()
    async def load(self, ctx, *, module):
        try:
            self.bot.load_extension(f'cogs.{module}')
        except commands.ExtensionError as e:
            await ctx.send(f'{e.__class__.__name__}: {e}')
        else:
            await ctx.send(f'Loaded cog: {module}')

    @commands.command(name='unload')
    @commands.is_owner()
    async def unload(self, ctx, *, module):
        try:
            self.bot.unload_extension(f'cogs.{module}')
        except commands.ExtensionError as e:
            await ctx.send(f'{e.__class__.__name__}: {e}')
        else:
            await ctx.send(f'Unloaded cog: {module}')


def setup(bot):
    bot.add_cog(Main(bot))