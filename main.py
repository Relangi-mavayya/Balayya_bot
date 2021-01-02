import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='b')

@client.event
async def on_ready():
    print('Bot is ready')

dailouge_pics =[
'https://cdn.discordapp.com/attachments/794846731296178207/794872496503259166/B-10.png', 
'https://cdn.discordapp.com/attachments/794846731296178207/794872477376315432/B-2.png',
'https://cdn.discordapp.com/attachments/794846731296178207/794872462164623370/B-3.png',
'https://cdn.discordapp.com/attachments/794846731296178207/794872462164623370/B-3.png',
'https://cdn.discordapp.com/attachments/794846731296178207/794872423216185384/B-4.png',
'https://cdn.discordapp.com/attachments/794846731296178207/794872443185528842/B-5.png',
'https://cdn.discordapp.com/attachments/794846731296178207/794872401858002974/B-6.png',
'https://cdn.discordapp.com/attachments/794846731296178207/794872385815183390/B-7.png',
'https://cdn.discordapp.com/attachments/794846731296178207/794872366248624128/B-8.png',
'https://cdn.discordapp.com/attachments/794846731296178207/794872352939835403/Balayyya-Babu.png'
]           #List of pictures


@client.command()
async def alayya(ctx):
    embed = discord.Embed(description = '__**Jai Balayya**__', color = discord.Color.red())
    random_link = random.choice(dailouge_pics)
    embed.set_image(url= random_link)
    await ctx.send(embed = embed)



client.run('token')
