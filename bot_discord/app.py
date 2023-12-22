import discord
import os
import logging

from src.event import Event
from dotenv import load_dotenv
from discord.ext import commands



load_dotenv()

intents = discord.Intents.default()
intents.messages = True  
intents.guilds = True 
intents.reactions = True 

client = commands.Bot(command_prefix="<", case_insensitive=True,intents=intents)
# client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logging.info(f'We have logged in as {client.user}')
   
@client.event
async def on_message(message):
    # print(f'message: {message.content}')
    message = await message.channel.fetch_message(message.id) # gets the message with id

    # logging.info(f'server: {message.guild}, user: {message.author}')# , nick: {message.author.nick}' 
    event = Event(message, client)
    await event.bot_replies()
    
logging.basicConfig(filename='bot_discord/environment/dev/bot.log', level=logging.DEBUG)  # Đổi INFO thành DEBUG để log cả các thông điệp debug.
client.run(os.getenv('TOKEN_DISCORD_BOT'), reconnect = True) 

