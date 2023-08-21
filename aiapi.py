import openai
import config
openai.api_key = config.DevelopmentConfig.OPENAI_KEY 


messages= [{"role": "system", "content": "You are a mental health counsolor."}]
def generateChatResponse(prompt):

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)

    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)
    
    try:
        answer = response['choices'][0]['message']['content'].replace('\n', '<br>')
    except:
        answer = "I'm sorry, I didn't understand that."
    
    return answer