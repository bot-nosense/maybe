from src.object_class.tarots import Tarots

def main():

    while True:
        try:
            nb_of_card = int(input("Số lá muốn rút: "))
            if nb_of_card > 0:
                break
            else:
                print("Số lá phải lớn hơn 0. Vui lòng nhập lại.")
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập lại.")

    a = input("Câu hỏi: ")
    card_list = []
    tarot = Tarots(nb_of_card= nb_of_card)

    for nb in range(nb_of_card):
        card = tarot.get_info_card()
        if (card in card_list) == False: 
            card_list.append( tarot.get_info_card() )

    for card in card_list:
        print(f"Card: {card[0]} - {card[1]}")

    
