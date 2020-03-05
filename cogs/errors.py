import traceback
import sys
from discord.ext import commands
import discord


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        error = getattr(error, 'original', error)

        if isinstance (error, commands.DisabledCommand):
            return await ctx.send(f'`{ctx.command}` has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.author.send(f'`{ctx.command}` can not be used in DMs')
            except:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                return await ctx.send('Member not found. Try again')

        elif isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send(f'`{ctx.command}` requires an argument')

        elif isinstance(error, commands.BotMissingPermissions):
            return await ctx.send(str(error))

        elif isinstance(error, commands.NotOwner):
            return await ctx.send(str(error))

        elif isinstance(error):
            return await ctx.send(str(error))

        print('Exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(ErrorHandler(bot))