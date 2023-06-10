from src.utils.functions.reading_the_deck import draw_tarot_cards, yes_no_question


def main():

    while True:
        try:
            print()
            choose = int(input("Chọn: 1-Yes/No  2-Rút lá: "))
            if choose > 0: 
                question = input("Câu hỏi: ")
                if choose == 1: yes_no_question(question)
                elif choose == 2: draw_tarot_cards()
            else: return "Số lá phải lớn hơn 0. Vui lòng nhập lại."
        except ValueError: return "Đầu vào không hợp lệ. Vui lòng nhập lại."



    

    
    
    

    
