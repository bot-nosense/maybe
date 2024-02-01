import random as rd
import os
import discord as dc

from data_core.input_data import input_data_json
from data_core.qoute import blame
from data_core.commands import * 
from dotenv import load_dotenv
from collections import defaultdict
from datetime import datetime, timedelta
from algorithm_core.yes_no_questions import YesNoQuestions

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

    def check_validate_commands(self, commands):
        return next((i for i in commands if i in self.message.content), None)

    def concat_commands(self):
        # split commands, self.message
        
        pass

    def tag_user(self):
        return self.message.author.mention

    def get_card_list(self, count):
        
        keys = set()
        while len(keys) < count:
            num = rd.randint(1, 158)
            if num % 2 != 0 and num + 1 not in keys: # không có cùng lá khác status trong list
                keys.add(num)
            elif num - 1 not in keys:
                keys.add(num)
        keys = list(keys)

        selected_values = [input_data_json[str(key)] for key in keys if str(key) in input_data_json]
        self.names = [i[1] for i in selected_values]
        self.url_img = [( str(os.getenv('DATABASE_VISION_TAROT')) + str(i[0]) ) for i in selected_values]

    def format_items(self, items):
        formatted_items = ', \n'.join(items)
        return formatted_items

    def card_name(self):
        return self.format_items(self.names)

    def card_image(self):
        return self.format_items(self.url_img)

    def random_replies(self, list):
        return rd.choice(list)
        pass

    def save_file(self, question, url):
        with open(url, 'a', encoding='utf-8') as f:
            f.write(question + '\n')

    async def bot_replies(self):

        input_message = self.message.content.lower()
        content = self.check_validate_commands(MAIN_COMMANDS)
        blame_content = self.check_validate_commands(blame.keys())
        request_user_path=os.getenv('REQUEST_USER_PATH')

        if self.message.author == self.client.user:
            return 
        
        if self.message.content != None:
            for keyword, response in blame.items():
                if input_message.startswith(keyword) or blame_content == keyword:
                    message_content = self.random_replies(response)
                    await self.message.reply(content=message_content)
                    break

            if self.message.content.startswith(MAIN_COMMANDS[0]) or content == MAIN_COMMANDS[0] or content == MAIN_COMMANDS[4]: 
                self.save_file(self.message.content, request_user_path) 
                nb = 1
                self.get_card_list(nb)
                YesNo = YesNoQuestions(self.get_card_name())

                yesno_content = YesNo.face_up()
                card_name_content = self.card_name()
                message_content = f'{card_name_content}\nThese {nb} cards mean: {yesno_content}'

                files = [dc.File(self.url_img[i]) for i in range(nb)]
                await self.message.reply(content=message_content, files=files)

            elif self.message.content.startswith(MAIN_COMMANDS[1]) or content == MAIN_COMMANDS[1] or content == MAIN_COMMANDS[5]:
                self.save_file(self.message.content, request_user_path)   
                nb = 3
                self.get_card_list(nb)
                YesNo = YesNoQuestions(self.get_card_name())
                
                yesno_content = YesNo.face_up()
                card_name_content = self.card_name()
                message_content = f'{card_name_content}\nThese {nb} cards mean: {yesno_content}' 

                files = [dc.File(self.url_img[i]) for i in range(nb)]
                await self.message.reply(content=message_content, files=files)

            elif self.message.content.startswith(MAIN_COMMANDS[2]) or content == MAIN_COMMANDS[2] or content == MAIN_COMMANDS[6]: 
                self.save_file(self.message.content, request_user_path) 
                nb = 6
                self.get_card_list(nb)
                message_content = self.card_name()
                files = [dc.File(self.url_img[i]) for i in range(nb)]
                await self.message.reply(content=message_content, files=files)

            elif self.message.content.startswith(MAIN_COMMANDS[3]) or content == MAIN_COMMANDS[3] or content == MAIN_COMMANDS[7]:  
                self.save_file(self.message.content, request_user_path) 
                nb = 9
                self.get_card_list(nb)
                message_content = self.card_name()
                files = [dc.File(self.url_img[i]) for i in range(nb)]
                await self.message.reply(content=message_content, files=files)

            elif self.message.content.startswith(MAIN_COMMANDS[3]) or content == MAIN_COMMANDS[10]:  
                self.save_file(self.message.content, request_user_path) 
                nb = 12
                self.get_card_list(nb)
                message_content = self.card_name()
                files = [dc.File(self.url_img[i]) for i in range(nb)]
                await self.message.reply(content=message_content, files=files)

            elif self.message.content.startswith(MAIN_COMMANDS[3]) or content == MAIN_COMMANDS[8] or content == MAIN_COMMANDS[9]:  
                self.save_file(self.message.content, request_user_path) 
                nb = 7
                self.get_card_list(nb)
                message_content = self.card_name()
                files = [dc.File(self.url_img[i]) for i in range(nb)]
                await self.message.reply(content=message_content, files=files)

            elif self.message.content.startswith(MAIN_COMMANDS[3]) or content == MAIN_COMMANDS[11] or content == MAIN_COMMANDS[12]:  
                self.save_file(self.message.content, request_user_path) 
                nb = 5
                self.get_card_list(nb)
                YesNo = YesNoQuestions(self.get_card_name())
                
                yesno_content = YesNo.face_up()
                card_name_content = self.card_name()
                message_content = f'{card_name_content}\nThese {nb} cards mean: {yesno_content}'

                files = [dc.File(self.url_img[i]) for i in range(nb)]
                await self.message.reply(content=message_content, files=files)

            else:
                # response = self.random_replies()
                # await self.message.reply(response)
                return
