import discord
import os
import logging
import datetime

from src.event import Event
from dotenv import load_dotenv
from discord.ext import commands



load_dotenv()

intents = discord.Intents.default()
intents.messages = True  
intents.guilds = True 
intents.reactions = True 


# client = commands.Bot(command_prefix="<", case_insensitive=True,intents=intents)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logging.info(f'We have logged in as {client.user}')
   
@client.event
async def on_message(message):

    message = await message.channel.fetch_message(message.id) # gets the message with id

    current_time = str(datetime.datetime.now())
    logging.info(f"{current_time}: User [{message.author.name}] in [{message.guild.name}] sent: [{message.content}]")
    
    event = Event(message, client)
    await event.bot_replies()
    
logging.basicConfig(filename='bot_discord/environment/dev/bot.log', level=logging.DEBUG, format='%(asctime)s: %(message)s', encoding='utf-8')  # Đổi INFO thành DEBUG để log cả các thông điệp debug.
client.run(os.getenv('TOKEN_DISCORD_BOT'), reconnect = True) 

