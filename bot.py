import discord
from discord.ext import commands
client = commands.Bot(command_prefix = "!")

#Copy token from discord developer portal and save it in TOKEN.txt

def read_token():
    with open("TOKEN.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

@client.event
async def on_ready():
    print('Bot is ready');

@client.command()
async def commands(ctx):
    await ctx.send("COMMAND LIST: \n\n !ping \n !kick \n !ban \n !unban \n !unbanall")

@client.command()
async def ping(ctx):
    await ctx.send(f'Your ping is {round(client.latency * 1000)} ms')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason = reason)
    await ctx.send(f'User {member} has been kicked from the server!')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason = reason)
    await ctx.send(f'User {member} has been banned from the server!')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discrim = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name,member_discrim):
            await ctx.guild.unban(user)
            await ctx.send(f'User {user.name}#{user.discriminator} has been unbanned!')
            return

@client.command()
async def unbanall(ctx):
    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)

    await ctx.send('All banned users have been unbanned!')


client.run(token)
