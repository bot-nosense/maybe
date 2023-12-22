import shutil



class Process:

    def __init__(self, question, answer, source_file_path):
        self.question = question
        self.answer = answer
        self.source_file_path = source_file_path
        # self.tar = Tarots(2)

    def save_excel_to_c_drive(self, source_file_path):
        # Đường dẫn đích - ở đây là C:/
        destination_path = 'C:/'

        # Kết hợp đường dẫn đích và tên file
        destination_file_path = f'{destination_path}craw_data_carot_vn_bot_nosense.xlsx'

        try:
            # Sao chép tệp từ nguồn đến đích
            shutil.copy(source_file_path, destination_file_path)
            print(f'Tệp {source_file_path} đã được sao chép đến {destination_file_path}')
        except Exception as e:
            print(f"Lỗi: {e}")

    # Sử dụng hàm để lưu tệp Excel
    source_file_path = 'environment\craw_data_carot_vn_bot_nosense.xlsx' 
    save_excel_to_c_drive(source_file_path)