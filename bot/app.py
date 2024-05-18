import discord
import os
import logging
import datetime

from src.event import Event
from dotenv import load_dotenv


# Start the system environment and install the base
load_dotenv()

intents = discord.Intents.default()
intents.messages = True  
intents.guilds = True 
intents.reactions = True 

log_format = "%Y-%m-%d %H:%M:%S"
client = discord.Client(intents=intents)
allowed_server_id = "YOUR_SERVER_ID"

# message_history = {}
# spam_threshold = 4  # Số tin nhắn tối đa trong khoảng thời gian để coi là spam
# spam_duration = 4  # Thời gian (giây) để xem xét số tin nhắn


@client.event
async def on_ready():
    logging.info(f'We have logged in as [{client.user}]')
   

@client.event
async def on_message(message):

    message = await message.channel.fetch_message(message.id) 
    event = Event(message, client)
    
    await event.bot_replies()
    

# run app
logging.basicConfig( 
    filename= os.getenv('LOG_PATH'), 
    level=logging.DEBUG,  
    format='%(asctime)s: %(message)s',  
    datefmt=log_format, 
    encoding='utf-8' 
)
client.run(os.getenv('DISCORD_TOKEN'), reconnect = True) 

