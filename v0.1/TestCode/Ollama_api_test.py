from ollama import chat

messages = [
  {
    'role': 'user',
    'content': '你好',
  },
]

response = chat('deepseek-r1:7b', messages=messages)
print(response['message']['content'])