dailouge_pics =[
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/Dialougepics/1.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/Dialougepics/10.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/Dialougepics/2.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/Dialougepics/3.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/Dialougepics/4.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/Dialougepics/5.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/Dialougepics/6.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/Dialougepics/7.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/Dialougepics/8.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/Dialougepics/9.jpg?raw=true'
]


greeting_gifs = [
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/greetpics/g1.gif?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/greetpics/g2.gif?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/greetpics/g3.gif?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/greetpics/g4.gif?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/greetpics/g5.gif?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/greetpics/g6.gif?raw=true'
]

import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='balayya ')

@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity=discord.Activity(type = discord.ActivityType.listening, name = 'balayya'))



@client.command()
async def balayya(ctx):
    embed = discord.Embed(description = '__**Jai Balayya**__', color = discord.Color.red())
    random_link = random.choice(dailouge_pics)
    embed.set_image(url= random_link)
    await ctx.send(embed = embed)

@client.command()
async def marriage(ctx):
    await ctx.send('https://kulfyapp.com/embed/2LN1DE')

@client.command(aliases = ['greet', 'namaskaram'])
async def namaste(ctx):
    embed = discord.Embed(description = '**Namaskaram :pray: **', color = discord.Color.red())
    random_greet = random.choice(greeting_gifs)
    embed.set_image(url= random_greet)
    await ctx.send(embed = embed)


"""list_commands = ['Here are the list of commands', '=balayya for random dailouge Pics']

@client.command()
async def commands(ctx):
    embed = discord.Embed(title= 'Commands', description= list_commands, color= discord.Color.red())
    embed.set_footer(icon_url=ctx.author.avatar_url, text= f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)"""

client.run('token')
