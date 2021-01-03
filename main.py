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


movie_dialouge =[
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/1-Legend.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/1.-Samara-Simha-Reddy.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/10-Veerabhadra..jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/10-narasimha-naidu.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/2-Simha%20(1).jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/2-simha.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/2-simha.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/3.-Lengend.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/4-Legend.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/4.-simha.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/4.-simha.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/5.-Neeku-bail-ippichindi.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/6-Gautami-Putra.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/6.-Nuvvu-bhayapedithe.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/7-Bobbili-Simham.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/7.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/8-Rowdy-Inspector.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/8.-Naku-emotions-Legend.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/9-Lion.jpg?raw=true',
'https://github.com/Relangi-mavayya/Balayya_bot/blob/main/Assets/moviedialogs/9.-Central-Legend.jpg?raw=true'
]


import discord
from discord.ext import commands
from discord.utils import get
import random

client = commands.Bot(command_prefix='balayya ')

@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity=discord.Activity(type = discord.ActivityType.listening, name = 'balayya'))


#for random fun dailouge pics
@client.command(aliases=['fun d', 'fd'])
async def fun(ctx):
    value = random.randint(0, 0xffffff)
    embed = discord.Embed(description = '__**Jai Balayya**__', color = value)
    random_link = random.choice(dailouge_pics)
    embed.set_image(url= random_link)
    await ctx.send(embed = embed)

#for marriage scene
@client.command(aliases=['marry'])
async def marriage(ctx):
    await ctx.send('https://kulfyapp.com/embed/2LN1DE')


#for random movie dailouge pics
@client.command(aliases=['movie d','md'])
async def movie(ctx):
    value = random.randint(0, 0xffffff)
    embed = discord.Embed(color = value) 
    random_movie_dialouge = random.choice(movie_dialouge)
    embed.set_image(url= random_movie_dialouge)
    await ctx.send(f'{ctx.author.mention}' , embed = embed)

#for random greets with that member mention
@client.command(aliases = ['namaskaram','Namaskaramd'])
async def namaste(ctx):
    value = random.randint(0, 0xffffff)
    embed = discord.Embed(description = '**Namaskaram :pray: **', color = value) 
    random_greet = random.choice(greeting_gifs)
    embed.set_image(url= random_greet)
    await ctx.send(f'{ctx.author.mention}' , embed = embed)

@client.command()
async def greet(ctx, arg):
    value = random.randint(0, 0xffffff)
    embed = discord.Embed(color = value) 
    random_greet = random.choice(greeting_gifs)
    embed.set_image(url= random_greet)
    embed.set_footer(icon_url=ctx.author.avatar_url, text= f'Requested by {ctx.author.name}')
    await ctx.send( str(arg)+ ' **Namaskaram :pray: **', embed = embed)

#if someone didnt mention someone
@client.event
async def on_command_error(ctx, error):
    msg= '**Evarinanna Mention chey ra**'
    value = random.randint(0, 0xffffff)
    embed = discord.Embed(description = msg, color = value)
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.mention}', embed=embed)
    

client.run('token')
