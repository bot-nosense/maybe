import random
from src.object_class.tarots import Tarots
from src.utils.constants import MEANING_TYPE, NATURE_TYPE, ONLY_MINOR_ARCANA_TYPE


def yes_no_question():

    tarot = Tarots(nb_of_card= 1)
    name_card = tarot.get_info_card()
    card_type = name_card.split(' - ')[1]
    options = random.randint(1, 3)
    print('Card:', name_card)

    def render_questions(card_list= None, card_type = None):
        if card_type in card_list: return card_list[card_type]
        else: return 'Good Luck! - chưa biết được Yes or No.'

    match options:
        case 1: 
            print( 'Type: MEANING - Theo tính chất của lá bài' )
            print( 'Result: ', render_questions(card_list= MEANING_TYPE, card_type= card_type) )
        case 2: 
            print( 'Type: NATURE - Chỉ có Yes hoặc No' )
            print( 'Result: ', render_questions(card_list= NATURE_TYPE, card_type= card_type) )
        case 3: 
            card_type = name_card.split(' - ')[0]
            sub_name = card_type.split(' ')[-1]
            print( 'Type: ONLY_MINOR_ARCANA - Chỉ có ẩn phụ' )
            print( 'Result: ', render_questions(card_list= ONLY_MINOR_ARCANA_TYPE, card_type= sub_name) )


def get_number_of_card():
    while True:
        try:
            nb_of_card = int(input("Số lá muốn rút: "))
            if nb_of_card > 0: return nb_of_card
            else: return "Số lá phải lớn hơn 0. Vui lòng nhập lại."
        except ValueError: return "Đầu vào không hợp lệ. Vui lòng nhập lại."


def draw_tarot_cards():
    number_of_card= get_number_of_card()
    tarot = Tarots(nb_of_card= number_of_card)
    card_list = []

    for nb in range(number_of_card):
        card = tarot.get_info_card()
        if (card in card_list) == False: 
            card_list.append( card )

    for card in card_list:
        print('Card: ', card)