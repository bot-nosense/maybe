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
        card = self.tar.print_result()
        print('-----')
        print('Card:        ',card)
        
        def result(card):
            card = [part.strip() for part in card.split('-')]
            minor_arcana = card[0].split(' ')
            len_minor_arcana = len(minor_arcana)
            if len_minor_arcana == 3:
                if card[0] == 'The Hanged Man': return YES_NO_QUES['NATURE_TYPE'][card[1]]
                else:
                    match random_case:
                        case 'NATURE_TYPE': return YES_NO_QUES['NATURE_TYPE'][card[1]] 
                        case 'ONLY_MINOR_ARCANA_TYPE': return YES_NO_QUES['ONLY_MINOR_ARCANA_TYPE'][minor_arcana[2]] 
                        case 'MEANING_TYPE': 
                            if minor_arcana[2] in {'Swords', 'Pentacles', 'Chalices', 'Cups', 'Wands'}: return YES_NO_QUES['MEANING_TYPE'][minor_arcana[2]]
                            else: return YES_NO_QUES['MEANING_TYPE']['minor_arcana']
            else: return YES_NO_QUES['NATURE_TYPE'][card[1]]  

        def print_result(card):
            print('Result:      ', result(card))

        return print_result(card)





















