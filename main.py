import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='=')

@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity=discord.Activity(type = discord.ActivityType.listening, name = 'balayya'))


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

Greeting_gifs = [
'https://tenor.com/view/namaste-hii-hello-namaskharam-gif-gif-18337586'
'https://tenor.com/view/namaste-nbk-balayya-gif-thank-you-gif-18483316'
'https://tenor.com/view/balayya-balakrishna-legend-gif-19115307'
'https://tenor.com/view/namaskaram-namaste-hi-hello-balayya-gif-19087108'
'https://tenor.com/view/hai-hi-hello-bala-krishna-gif-gif-18338525'
'https://tenor.com/view/hai-hii-hi-hello-tata-gif-18338504'
'https://tenor.com/view/nandamuri-balakrishna-says-assalaam-alaikum-nbk-balakrishna-gif-trending-gif-18337406'
]



@client.command()
async def balayya(ctx):
    embed = discord.Embed(description = '__**Jai Balayya**__', color = discord.Color.red())
    random_link = random.choice(dailouge_pics)
    embed.set_image(url= random_link)
    await ctx.send(embed = embed)

@client.command()
async def marriage(ctx):
    await ctx.send('https://kulfyapp.com/embed/2LN1DE')

@client.command()


#list_commands = ['Here are the list of commands', '=balayya for random dailouge Pics']

#@client.command()
#async def commands(ctx):
    #embed = discord.Embed(title= 'Commands', description= list_commands, color= discord.Color.red())
    #embed.set_footer(icon_url=ctx.author.avatar_url, text= f'Requested by {ctx.author.name}')
    #await ctx.send(embed=embed)

client.run('token')
