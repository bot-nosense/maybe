from src.utils.functions import draw_tarot_cards, yes_no_question

def main():

    while True:
        try:
            choose = int(input("Chọn thể loại 1-Yes/No  2-Rút lá: "))
            if choose > 0: 
                question = input("Câu hỏi: ")
                if choose == 1: return yes_no_question()
                elif choose == 2: return draw_tarot_cards()
            else: return "Số lá phải lớn hơn 0. Vui lòng nhập lại."
        except ValueError: return "Đầu vào không hợp lệ. Vui lòng nhập lại."
    
    
    

    
