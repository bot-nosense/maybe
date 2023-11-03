from src.object_class.process import Process 


def main():
    print('beta verison 0.0.0.3, 20231031 update yes/no questions')

    while True:
        try:
            print()
            # choose = int(input("Chọn: 1-Yes/No  2-Rút lá: "))
            # if choose > 0: 
            # if choose ==  1: 
            question = input("Question:     ")
            pr = Process(question)
            pr.yes_no_question(question)
            # if choose == 1: pr.yes_no_question(question)
            # elif choose == 2: pr.draw_tarot_cards()
            # else: return "Lớn hơn 0, nhập lại đê."
        except ValueError: return "Nhập lại đê." 



    

    
    
    

    
