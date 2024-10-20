import os
import openai

def open_ai_prompt_request(model_name, content,system_prompt):
    API_KEY = os.environ.get('OPENAI_API_KEY')
    if not API_KEY:
        raise ValueError("OPENAI_API_KEY environment variable not found")
    
    open_ai_client = openai.OpenAI(api_key=API_KEY)
    user_message = [{"role": "user", "content": content}] 
    messages = system_prompt + user_message
    response = open_ai_client.chat.completions.create(messages=messages, model=model_name)
    return response

def open_ai_get_response_content(openai_response):
    translation = openai_response.choices[0].message.content
    return translation    