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

slogans=[
'**Jublie hills Banjara hills Balayya kodithe hospital bills**',
'**Hyderabad secunderabad balayya Babu zindabad**',
'**Ramudu beemudu ma balayya Babu demudu**',
'**Oopu groupu balayya Babu thopu**',
'**Varshakalam lo current kotha Ammaila gundello balayya Babu motha**',
'**India ki pm modi industry ki balayya Babu daddy**',
'**1234 balayya never before**',
'**Maza frooti balayya Babu naughty**',
'**Jiljil jiga ma balayya Babu sega**',
'**Uppukaaram balayya meda chaavadu ma mamakaram**',
'**Paina kinda oopu balayya Babu thopu**'
]

import discord
from discord.ext import commands
from discord.utils import get
import random

client = commands.Bot(command_prefix='balayya ', case_insensitive=True, help_command=None)

@client.event
async def on_ready():
    print('Balayya on grounds')
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
    await ctx.send( '**Namaskaram :pray: ** ' +str(arg) , embed = embed)

#if someone didnt mention someone
@client.event
async def on_command_error(ctx, error):
    msg= '**Evarinanna Mention chey ra**'
    value = random.randint(0, 0xffffff)
    embed = discord.Embed(description = msg, color = value)
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.mention}', embed=embed)


#for random fun dailouge pics
@client.command(aliases=['s',])
async def slogan(ctx):
    value = random.randint(0, 0xffffff)
    random_slogan = random.choice(slogans)
    embed = discord.Embed(description = random_slogan, color = value)
    await ctx.send(embed = embed)



"""# My sample help command:
@client.command(aliases=['help','h'])
async def _help(ctx, args=None):
    help_embed = discord.Embed(title="Balayya Help Commands")
    command_names_list = [x.name for x in bot.commands]

# If there are no arguments, just list the commands:
if not args:
    help_embed.add_field(name="List of supported commands:", value="\n".join([str(i+1)+". "+x.name for i,x in enumerate(bot.commands)]),inline=False)
    help_embed.add_field(name="Details", value="Type `.help <command name>` for more details about each command.", inline=False)

# If the argument is a command, get the help text from that command:
elif args in command_names_list:
    help_embed.add_field(name=args, value=bot.get_command(args).help)

# If someone is just trolling:
else:
    help_embed.add_field(name="Nope.", value="Don't think I got that command, boss!")
    await ctx.send(embed=help_embed)"""


class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.blurple(), description='__**Balayya a telugu film god**__ \n') 
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

client.help_command = MyHelpCommand()


client.run('token')
