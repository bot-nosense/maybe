from src.object_class.process import Process 


def main():

    while True:
        try:
            print()
            choose = int(input("Chọn: 1-Yes/No  2-Rút lá: "))
            if choose > 0: 
                question = input("Câu hỏi: ")
                pr = Process(question)
                if choose == 1: pr.yes_no_question(question)
                elif choose == 2: pr.draw_tarot_cards()
            else: return "Lớn hơn 0, nhập lại đê."
        except ValueError: return "Nhập lại đê." 



    

    
    
    

    
