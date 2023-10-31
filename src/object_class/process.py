import random
from src.utils.constants import YES_NO_QUES
from src.object_class.tarots import Tarots 


class Process:

    def __init__(self, question):
        self.question = question
        self.tar = Tarots(2)

    def draw_tarot_cards(self):
        print('1')

    def yes_no_question(self, question):
        random_case = random.choice(list(YES_NO_QUES.keys()))
        card = self.tar.get_info_card()
        print('Lá bài: ', card)

        def result(card_name):
            card_name = [part.strip() for part in card_name.split('-')]
            minor_arcana_name = card_name[0].split(' ')
            len_minor_arcana = len(minor_arcana_name)
            if len_minor_arcana == 3:
                if card_name[0] == 'The Hanged Man': return YES_NO_QUES['NATURE_TYPE'][card_name[1]]
                else:
                    match random_case:
                        case 'NATURE_TYPE': return YES_NO_QUES['NATURE_TYPE'][card_name[1]] 
                        case 'ONLY_MINOR_ARCANA_TYPE': return YES_NO_QUES['ONLY_MINOR_ARCANA_TYPE'][minor_arcana_name[2]] 
                        case 'MEANING_TYPE': return YES_NO_QUES['MEANING_TYPE'][minor_arcana_name[2]]
            else: return YES_NO_QUES['NATURE_TYPE'][card_name[1]]  

        def print_result(card_name):
            print(result(card_name))

        return print_result(card)





















