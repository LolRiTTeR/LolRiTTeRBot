import discord
import datetime

from discord.ext import commands


class Help(commands.Cog, name='help'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help', hidden=True)
    @commands.bot_has_permissions(embed_links=True)
    async def help(self, ctx):
        embed = discord.Embed(title='Command list')
        local_commands = []
        local_description = []
        for cmd in self.bot.walk_commands():
            if not cmd.hidden and cmd.name not in str(local_commands):
                temp = f'{cmd.name}'
                if cmd.aliases:
                    for alias in cmd.aliases:
                        temp += f', {alias}'
                local_commands.append(f'`{temp}`')
                local_description.append(f'`{cmd.description}`')
        local_commands, local_description = zip(*sorted(zip(local_commands, local_description)))
        embed.add_field(name='Command', value="\n".join(local_commands), inline=True)
        embed.add_field(name='Description', value="\n".join(local_description), inline=True)
        embed.set_footer(text='LolRiTTeRBot', icon_url=self.bot.user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
