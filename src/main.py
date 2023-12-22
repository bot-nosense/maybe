from src.object_class.process import Process 
from flask import Flask
from src.web.routes import app



def main():
    print('beta verison 0.0.0.4: Develop card drawing feature on local website')

    # while True:
    try:
        print()
        print("Mục lục:\n    1. Câu hỏi yes/no\n    2. Rút lá")
        choose = int(input("Nhập lựa chọn: "))
        match choose:
            case 1:
                question = input("Question:     ")
                pr = Process(question)
                pr.yes_no_question(question)
            case 2: pass
            case _:
                print('----')
    except ValueError: return "Nhập lại đê." 



    

    
    
    

    
