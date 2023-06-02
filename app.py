import random
import os
import re


class Tarots:

    def __init__(self, nb_of_card = None):
        """
        Khởi tạo class Tarots với số lá bài được nhập vào 
        và dictionary chứa thông tin các lá bài.
        """
        
        self.nb_of_card = nb_of_card
        self.card_dict = {} # Khởi tạo dictionary để lưu thông tin lá bài

        path = "database/"
        files = os.listdir(path)
        for file in files:

            # Lấy key của lá bài từ tên file
            card = file.split(".jpg")[0] 
            card_full_name = card.split("-")
            card_number = card_full_name[0]
            card_name = re.sub('([a-z])([A-Z])', r'\1 \2', card_full_name[1])  # Lấy tên của lá bài từ key
            
            # Thêm key-value vào dictionary
            self.card_dict[card_number] = card_name 
        

    def get_info_card(self):
        """
        Hàm lấy thông tin của một lá bài trong bộ bài Tarot.
        Trả về tên và trạng thái của lá bài (xuôi hoặc ngược).
        """

        # Lấy số ngẫu nhiên từ 0 đến 78
        random_number = random.randint(0, 78) 

        # Lấy status ngẫu nhiên từ 0 hoặc 1
        random_status = random.randint(0, 1)

        # Lấy tên của lá bài từ dictionary
        card_name = self.card_dict[str(random_number)] 

        # Chuyển đổi giá trị của random_status thành chuỗi 'xuôi' hoặc 'ngược'
        card_status = 'xuôi' if random_status == 0 else 'ngược'
        
        return card_name, card_status
    

    def get_card(self):
        """
        Hàm lấy thông tin của nhiều lá bài trong bộ Tarot.
        Số lá bài được nhập vào khi khởi tạo class Tarots.
        Trả về một list các tuple chứa thông tin của các lá bài.
        """

        result = []
        for nb in range(self.nb_of_card):
            result.append( self.get_info_card() )

        return result



def main():
    """
    Hàm thực hiện in các lá bài và trạng thái của chúng,
    dựa trên câu hỏi nhập vào từ người dùng.
    """

    # Nhập vào câu hỏi
    a = input("Nhập vào câu hỏi: ")

    # Khởi tạo class Tarots và lấy thông tin của các lá bài
    tarot = Tarots(nb_of_card= 3)
    card_info = tarot.get_card() 

    # In thông tin của các lá bài
    for card in card_info:
        print(f"Card: {card[0]} - {card[1]}")


if __name__== "__main__":
    main()
