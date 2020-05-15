import os
import json
import discord
from dotenv import load_dotenv
from discord.ext import commands
from itertools import cycle

client = commands.Bot(command_prefix='t!')
os.chdir(os.getcwd())

# Cog loading
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# Console messages
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('t!help | https://cutt.ly/tc-326'))
    print(f'{client.user.name} is connected')

# Levelling
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'**Welcome to the Galactic Republic!**\n\nMake sure to check #rules before ' +
        'you start talking.\n\nAlso, please keep in mind that the server is still ' +
        'in testing, so ranks are temporary until the server is fully released! DM @TearyPanda#4202 if you have any questions!'
    )
    with open('users.json', 'r') as f:
        users = json.load(f)
    await update_data(users, member)
    with open('users.json', 'w') as f:
        json.dump(users, f)

@client.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)
        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)
        with open('users.json', 'w') as f:
            json.dump(users, f)
    await client.process_commands(message)

async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1

async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp

async def level_up(users, user, message):
    channel = client.get_channel(567197512851783680)
    guild = discord.utils.get(client.guilds, name='The Galactic Republic')
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1/3))
    if lvl_start < lvl_end:
        await channel.send(f'{user.mention} has leveled up to level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_start + 1
        if (lvl_end >= 5 and not discord.utils.get(guild.roles, name='Private') in user.roles):
            await user.add_roles(discord.utils.get(guild.roles, name='Private'))
            await channel.send(f'{user.mention} has ranked up to **Private**!')
        elif (lvl_end >= 10 and not discord.utils.get(guild.roles, name='Corporal') in user.roles):
            await user.add_roles(discord.utils.get(guild.roles, name='Corporal'))
            await channel.send(f'{user.mention} has ranked up to **Corporal**!')
        elif (lvl_end >= 15 and not discord.utils.get(guild.roles, name='Sergeant') in user.roles):
            await user.add_roles(discord.utils.get(guild.roles, name='Sergeant'))
            await channel.send(f'{user.mention} has ranked up to **Sergeant**!')
        elif (lvl_end >= 20 and not discord.utils.get(guild.roles, name='Arc Trooper') in user.roles):
            await user.add_roles(discord.utils.get(guild.roles, name='Arc Trooper'))
            await channel.send(f'{user.mention} has ranked up to **Arc Trooper**!')
        elif (lvl_end >= 25 and not discord.utils.get(guild.roles, name='Captain') in user.roles):
            await user.add_roles(discord.utils.get(guild.roles, name='Captain'))
            await channel.send(f'{user.mention} has ranked up to **Captain**!')
        elif (lvl_end >= 30 and not discord.utils.get(guild.roles, name='Commander') in user.roles):
            await user.add_roles(discord.utils.get(guild.roles, name='Commander'))
            await channel.send(f'{user.mention} has ranked up to **Commander**!')
        elif (lvl_end >= 35 and not discord.utils.get(guild.roles, name='Admiral') in user.roles):
            await user.add_roles(discord.utils.get(guild.roles, name='Admiral'))
            await channel.send(f'{user.mention} has ranked up to **Admiral**!')

# Errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments.')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission for this command.')
    elif isinstance(error, commands.NotOwner):
        await ctx.send('You do not have permission for this command.')





client.run('______')
