import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle


client =commands.Bot(command_prefix = '.')                                                                     #prefix to start the command as .(command) without brackets
status = cycle(['Need For Speed HEAT', 'PUBG MOBILE', 'Assassins Creed Origins','The Witcher 3: Wild Hunt'])

players = {}



@client.event                                                                  #to know if bots working or not              
async def on_ready():
   change_status.start()
   print('I am ONLINE.\nYou can now access ME to your hearts content :)')


@tasks.loop(seconds=20)                                                        #to change the activity of my bot 
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

 
@client.event
async def on_member_join(member):                                             #joined member notification     
    print(f'{member} has joined the server.')

@client.event                                                                 #leave member notification                       
async def on_member_remove(member):
     print(f'{member} has left the server.')


@client.command()                                                             #to ping as pong  .ping
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()                                                             #to clear the messages  .clear   
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

def is_it_me(ctx):
    return ctx.author.id == 562187252394885120

@client.command()
@commands.check(is_it_me)
async def check(ctx):
    await ctx.send(f'Hi {ctx.author}')



@client.command()                                                             #to kick out any member .kick@anyone
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()                                                             #to ban any member .ban@anyone
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command(aliases=['8ball', 'test'])                                    #for fun command .8ball
async def _8ball(ctx, *, question):
    responses = ['It is certain!',
                 'It is decidedly so!',
                 'Without a doubt!',
                 'Yes, definitely follow the force!',
                 'As I see it, yes!',
                 'Most likely!',
                 'Outlook good!',
                 'YES!',
                 'Signs point to yes!',
                 'Reply hazy, try again!',
                 'Ask again later!',
                 'Better not tell you now!',
                 'Cannot predict now!',
                 'Concentrate and ask again!',
                 'OOF, Dont count on it!',
                 'My reply is SIKE!',
                 'My sources say NO!',
                 'Outlook not so good!',
                 'Very Doubtful!']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


client.run('NjM3NTU0NzUwNTUxNzUyNzA1.XgxN4Q.fJiGF8Cgq0Qc4ntMRk4hzJw-cJY')                     #your bots tokken goes here 'token'
