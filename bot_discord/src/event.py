import random as rd
import os
import discord

from src.constants import RANDOM_QOUTE, VISION_TAROT_JSON
from dotenv import load_dotenv

load_dotenv()


class Event:

    def __init__ (self, message, client):
        self.message = message
        self.client = client
        self.names = []
        self.url_img = []

    def get_card_name(self):
        return self.names

    def get_path_img(self):
        return self.url_img

    def get_card_list(self, count):
        keys = [rd.randint(1, 158) for _ in range(count)]
        selected_values = [VISION_TAROT_JSON[str(key)] for key in keys if str(key) in VISION_TAROT_JSON]
        self.names = [i[1] for i in selected_values]
        self.url_img = [( str(os.getenv('DATABASE_VISION_TAROT')) + str(i[0]) ) for i in selected_values]

    def card_name(self):
        names = [name for name in self.names]
        result = ', \n'.join(names)
        return result
    
    def card_image(self):
        paths = [path for path in self.url_img]
        result = ', \n'.join(paths)
        return result

    def random_replies(self):
        return rd.choice(RANDOM_QOUTE)

    async def bot_replies(self):
        if self.message.author == self.client.user:
            return 

        if self.message.content.startswith('1 lá'):  
            self.get_card_list(1)
            await self.message.channel.send(self.card_name())
            await self.message.channel.send(file=discord.File(self.card_image()))

        elif self.message.content.startswith('3 lá'):  
            self.get_card_list(3)
            await self.message.channel.send(self.card_name())
            files = []
            for i in range(3):
                files.append(discord.File(self.url_img[i]))
            await self.message.channel.send(files=files)

        elif self.message.content.startswith('6 lá'):  
            self.get_card_list(6)
            await self.message.channel.send(self.card_name())
            files = []
            for i in range(6):
                files.append(discord.File(self.url_img[i]))
            await self.message.channel.send(files=files)

        elif self.message.content.startswith('9 lá'):  
            self.get_card_list(9)
            await self.message.channel.send(self.card_name())
            files = []
            for i in range(9):
                files.append(discord.File(self.url_img[i]))
            await self.message.channel.send(files=files)

        else:
            response = self.random_replies()
            await self.message.channel.send(response)
            # return
