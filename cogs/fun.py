from random import randint
from discord.ext import commands

import aiohttp
import discord
import json


class Fun(commands.Cog, name='fun'):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def fetch(session, url):
        async with session.get(url) as response:
            return await response.text()

    @commands.command(name='penis', description='What do you think it will do?')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def penis(self, ctx):
        rnd = randint(1, 30)
        e = discord.Embed(description=f'8{"="*rnd}D', color=0x17c400)
        await ctx.send(embed=e)
        if rnd == 1:
            await ctx.send(f'<@!{ctx.author.id}> U hav smol pp :frowning:')

    @commands.command(name='fact', description='Gives a random (useless) fact')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def fact(self, ctx):
        async with aiohttp.ClientSession() as session:
            body = await self.fetch(session, 'https://useless-facts.sameerkumar.website/api')
            fact = json.loads(body)
            e = discord.Embed(description=f'{fact["data"]}', color=0x17c400)
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Fun(bot))
