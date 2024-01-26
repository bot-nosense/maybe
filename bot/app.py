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

log_format = "%Y-%m-%d %H:%M:%S"

client = discord.Client(intents=intents)

message_history = {}
spam_threshold = 4  # Số tin nhắn tối đa trong khoảng thời gian để coi là spam
spam_duration = 4  # Thời gian (giây) để xem xét số tin nhắn


async def check_spam(message, message_history):
    author_id = message.author.id
    author_id = str(author_id)
    if author_id not in message_history:
        message_history[author_id] = []  # Tạo danh sách trống nếu chưa có
    message_history[author_id].append(message.content)  # Thêm tin nhắn vào danh sách
    if len(message_history[author_id]) > spam_threshold:
        message_history[author_id] = []  # Đặt danh sách tin nhắn về trạng thái trống
        await message.channel.send(f'<@{author_id}>, nhắn ít thôi, thích spam không')

@client.event
async def on_ready():
    logging.info(f'We have logged in as [{client.user}]')
   
@client.event
async def on_message(message):
    message = await message.channel.fetch_message(message.id) # gets the message with id
    logging.info(f"User [{message.author.name}] sent: [{message.content}]               - {message}")
    event = Event(message, client)
    # await check_spam(message, message_history)
    await event.bot_replies()
    
logging.basicConfig(
    filename= os.getenv('LOG_PATH'),
    level=logging.DEBUG, 
    format='%(asctime)s: %(message)s', 
    datefmt=log_format,
    encoding='utf-8'
)
client.run(os.getenv('TOKEN_DISCORD'), reconnect = True) 

