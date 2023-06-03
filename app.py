from src.main import main

if __name__== "__main__":
    # main()
    import requests

    def chat_with_gpt(message):
        api_key = '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'
        url = 'https://api.openai.com/v1/chat/completions'
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        
        data = {
            'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'},
                        {'role': 'user', 'content': message}]
        }
        
        response = requests.post(url, json=data, headers=headers)
        response_data = response.json()
        
        if 'choices' in response_data:
            choices = response_data['choices']
            if choices and 'message' in choices[0]:
                return choices[0]['message']['content']
        
        return "Ê mầy, tôi không có hiểu."

    # Gửi tin nhắn cho ChatGPT và nhận phản hồi
    user_message = input("Nhập tin nhắn của bạn: ")
    response = chat_with_gpt(user_message)
    print(response)
