import discord
import datetime

from discord.ext import commands


class Help(commands.Cog, name='help'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help2', description='I want to see this description somewhere')
    @commands.bot_has_permissions(embed_links=True)
    async def help(self, ctx):
        embed = discord.Embed(title='Command list')
        names = ''
        descriptions = ''
        for cmd in self.bot.walk_commands():
            if cmd.description:
                names += f'{cmd.name}\n'
                descriptions += f'{cmd.description}\n'
        embed.add_field(name='\u200b', value=names, inline=True)
        embed.add_field(name='\u200b', value=descriptions, inline=True)
        embed.set_footer(text='LolRiTTeRBot', icon_url=self.bot.user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
