import random as rd
import os
import discord

from src.constants.vison_tarot import VISION_TAROT_JSON
from src.constants.qoute import RANDOM_QOUTE
from src.constants.commands import *
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

    def check_validate_commands(self):
        return next((i for i in MAIN_COMMANDS if i in self.message.content), None)


    def concat_commands(self):
        # split commands, self.message
        
        pass
    

    def tag_user(self):
        return self.message.author.mention

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

        content = self.check_validate_commands()

        if self.message.content.startswith(MAIN_COMMANDS[0]) or content == MAIN_COMMANDS[0] or content == MAIN_COMMANDS[4]:  
            nb = 1
            self.get_card_list(nb)
            message_content = self.card_name()
            files = [discord.File(self.url_img[i]) for i in range(nb)]
            await self.message.reply(content=message_content, files=files)

        elif self.message.content.startswith(MAIN_COMMANDS[1]) or content == MAIN_COMMANDS[1] or content == MAIN_COMMANDS[5]:  
            nb = 3
            self.get_card_list(nb)
            message_content = self.card_name()
            files = [discord.File(self.url_img[i]) for i in range(nb)]
            await self.message.reply(content=message_content, files=files)

        elif self.message.content.startswith(MAIN_COMMANDS[2]) or content == MAIN_COMMANDS[2] or content == MAIN_COMMANDS[6]: 
            nb = 6
            self.get_card_list(nb)
            message_content = self.card_name()
            files = [discord.File(self.url_img[i]) for i in range(nb)]
            await self.message.reply(content=message_content, files=files)

        elif self.message.content.startswith(MAIN_COMMANDS[3]) or content == MAIN_COMMANDS[3] or content == MAIN_COMMANDS[7]:  
            nb = 9
            self.get_card_list(nb)
            message_content = self.card_name()
            files = [discord.File(self.url_img[i]) for i in range(nb)]
            await self.message.reply(content=message_content, files=files)

        else:
            # response = self.random_replies()
            # await self.message.reply(response)
            return
