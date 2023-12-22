# Đường dẫn đến thư mục chứa ảnh của bạn
folder_path = 'C:/BOT Nosense/_projects/carot.vn/db_temp'

# Lấy danh sách các tệp trong thư mục
file_list = os.listdir(folder_path)

# print(f'os.path.join(folder_path, filename), {os.path.join(folder_path)}')

# Mẫu tên mới bạn muốn đặt lại
new_name_template = '{:01d}.jpg'  # Định dạng mẫu tên mới, ví dụ: new_file_001.jpg

a = 74
# Lặp qua từng tệp và đổi tên
for index, filename in enumerate(file_list):
    new_filename = str(a+1) + '.jpg'
    os.rename(os.path.join(str(folder_path), str(filename)), os.path.join(str(folder_path), str(new_filename)))
    a +=1