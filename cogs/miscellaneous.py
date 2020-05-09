import discord
import random
from discord.ext import commands

class Miscellaneous(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands

    @commands.command(name='ping', help='Responds with the latency')
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.command(name='8ball', help='Responds with a random answer to a question')
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt',
                     'Yes - definintely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     "Don't count on it.",
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook is not so good.',
                     'Very doubtful.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    # Errors
    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify a question.')

def setup(client):
    client.add_cog(Miscellaneous(client))
