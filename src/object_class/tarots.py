import random
import os
import re

class Tarots:

    def __init__(self, nb_of_card = None):
        
        self.nb_of_card = nb_of_card
        self.card_dict = {} # Lưu thông tin lá bài
        path = "database/"
        files = os.listdir(path)

        for file in files:
            card = file.split(".jpg")[0] 
            card_full_name = card.split("-")
            card_number = card_full_name[0]
            card_name = re.sub('([a-z])([A-Z])', r'\1 \2', card_full_name[1])  # Lấy tên của bài
            self.card_dict[card_number] = card_name 
        

    def get_info_card(self):

        random_number = random.randint(0, 78) 
        random_status = random.randint(0, 1)
        card_name = self.card_dict[str(random_number)] # Lấy tên của lá bài từ dictionary
        card_status = 'xuôi' if random_status == 0 else 'ngược'
        return card_name, card_status


    