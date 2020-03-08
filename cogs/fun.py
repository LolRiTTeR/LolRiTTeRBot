from random import randint
from urllib.request import urlopen

from discord.ext import commands

import discord
import json


class Fun(commands.Cog, name='fun'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='penis', description='What do you think it will do?')
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def penis(self, ctx):
        rnd = randint(1, 30)
        e = discord.Embed(description=f'8{"="*rnd}D', color=0x17c400)
        await ctx.send(embed=e)
        if rnd == 1:
            await ctx.send(f'<@!{ctx.author.id}> U hav smol pp :frowning:')

    @commands.command(name='fact', description='Gives a random (useless) fact')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def fact(self, ctx):
        url = urlopen('https://uselessfacts.jsph.pl/random.json?language=en', timeout=5)
        data = json.loads(url.read())
        print(data)
        e = discord.Embed(description='Placeholder', color=0x17c400)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Fun(bot))