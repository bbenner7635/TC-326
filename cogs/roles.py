import discord
from discord.ext import commands

class Roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == 567190262892462080:

            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

            blue = discord.utils.get(guild.roles, name='501st Legion')
            orange = discord.utils.get(guild.roles, name='212th Attack Battalion')
            grey = discord.utils.get(guild.roles, name='104th Battalion')
            red = discord.utils.get(guild.roles, name='Coruscant Guard')
            purple = discord.utils.get(guild.roles, name='187th Legion')

            if payload.emoji.name == '501st':
                role = blue
            elif payload.emoji.name == '212th':
                role = orange
            elif payload.emoji.name == '104th':
                role = grey
            elif payload.emoji.name == 'coruscantguard':
                role = red
            elif payload.emoji.name == '187th':
                role = purple
            else:
                role = discord.utils.find(lambda r : r.name == payload.emoji.name, guild.roles)

            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if (blue in member.roles or orange in member.roles or grey in member.roles or red in member.roles or purple in member.roles):
                    await member.create_dm()
                    await member.dm_channel.send(
                        f'You already have a role! Remove it before adding a new one.'
                    )
                    return
                await member.add_roles(role)
                await member.create_dm()
                await member.dm_channel.send(
                    f'You have been added to the {role.name} role.'
                )

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == 567190262892462080:

            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

            blue = discord.utils.get(guild.roles, name='501st Legion')
            orange = discord.utils.get(guild.roles, name='212th Attack Battalion')
            grey = discord.utils.get(guild.roles, name='104th Battalion')
            red = discord.utils.get(guild.roles, name='Coruscant Guard')
            purple = discord.utils.get(guild.roles, name='187th Legion')

            if payload.emoji.name == '501st':
                role = blue
            elif payload.emoji.name == '212th':
                role = orange
            elif payload.emoji.name == '104th':
                role = grey
            elif payload.emoji.name == 'coruscantguard':
                role = red
            elif payload.emoji.name == '187th':
                role = purple
            else:
                role = discord.utils.find(lambda r : r.name == payload.emoji.name, guild.roles)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.remove_roles(role)
            await member.create_dm()
            await member.dm_channel.send(
                f'You have been removed from the {role.name} role.'
            )

def setup(client):
    client.add_cog(Roles(client))
