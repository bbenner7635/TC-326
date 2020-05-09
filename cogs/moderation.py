import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self ,client):
        self.client = client

    # Commands
    @commands.command(name='clear', help='Clears the text channel of the previous # messages')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount)

    @commands.command(name='kick', help='Kicks a user from the server')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None): ##asterisk allows parameters to contain spaces
        await member.kick(reason=reason)

    @commands.command(name='ban', help='Bans a user from the server')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command(name='unban', help='Unbans a user from the server')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member): ##can't get discord.Member since they are not in the server
        banned_users = await ctx.guild.bans() ##named tuple
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    # Errors
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify a number of messages to delete.')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify a user.')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify a user.')

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify a user.')

def setup(client):
    client.add_cog(Moderation(client))
