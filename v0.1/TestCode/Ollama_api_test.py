from ollama import chat
think_switch , userinput= int(input('是否开启思维链(是输入1，否输入0)：')) , input('用户输入：')
messages = [
  {
    'role': 'user',
    'content': userinput,
  },
]
response = chat('deepseek-r1:7b', messages=messages, stream=True)

think_count = 0
def stream_print(response):
  global think_count
  global think_switch
  for messages in response:
    if think_switch==0:
      if think_count == 2:
        print(messages['message']['content'], end='', flush=True)
      if messages['message']['content'] == '<think>' or messages['message']['content'] == '</think>':
        think_count += 1
    else:
      print(messages['message']['content'], end='', flush=True)

stream_print(response=response)
