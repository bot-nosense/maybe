# from flask import Flask, render_template, request
# import os

# app = Flask(
#     __name__, 
#     template_folder=os.path.join(os.getcwd(), 'src/web/app/templates'),
#     static_folder=os.path.join(os.getcwd(), 'src/web/app/static')
# )

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     image_paths = ['0-TheFool-0.jpg']
#     image_name = ['asasfasf', 'af', 'ầ']

#     if request.method == 'POST':
#         nc = request.form.get('question')  # Lấy câu hỏi từ input
#         # Xử lý câu hỏi ở đây, ví dụ:
#         image_name.append('Label for the image')  # Thêm label cho ảnh

#     return render_template('index.html', image_paths=image_paths, image_name=image_name, number_card = nc)

# if __name__ == '__main__':
#     app.run(debug=True)


from app import app

if __name__ == '__main__':
    app.run(debug=True)