import discord
import os
import logging

from src.event import Event
from dotenv import load_dotenv



load_dotenv()

intents = discord.Intents.default()
intents.messages = True  
intents.guilds = True 
intents.reactions = True 

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logging.info(f'We have logged in as {client.user}')
   
@client.event
async def on_message(message):
    print(f'message: {message.content}')
    logging.info(f'server: {message.guild}, user: {message.author}')# , nick: {message.author.nick}' 
    event = Event(message, client)
    await event.bot_replies()
    
logging.basicConfig(filename='bot_discord/environment/dev/bot.log', level=logging.DEBUG)  # Đổi INFO thành DEBUG để log cả các thông điệp debug.
client.run(os.getenv('TOKEN_DISCORD_BOT'), reconnect = True) 

