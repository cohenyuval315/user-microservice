import os
import anthropic
from flask import current_app

class AnthropicAI:
    @classmethod
    def anthropic_request_prompt(cls,model_name:str, system_message: str, text_prompt: str, token_limit:int, stop_sequences: list[str] = None, temperature:float = 0.0):
        API_KEY = os.environ.get('ANTHROPIC_API_KEY')   
        if not API_KEY:
            raise ValueError("ANTHROPIC_API_KEY environment variable not found")    
        
        try:
            anthropic_client = anthropic.Anthropic(api_key=API_KEY)
            messages = [{"role": "user", "content": text_prompt}]
            params = {
                'model': model_name,
                'max_tokens': token_limit,
                'temperature':temperature,
                'system': system_message,
                'messages': messages
            }

            if stop_sequences is not None:
                params['stop_sequences'] = stop_sequences

            response = anthropic_client.messages.create(**params)
            return response
        except Exception as e:
            current_app.logger.error(e)

    @classmethod
    def anthropic_get_response_content(cls,anthropic_response):
        try:
            textblock = anthropic_response.content[0]
            text = textblock.text
            return text
        except Exception as e:
            current_app.logger.error(e)




def anthropic_request_prompt(model_name:str, system_message: str, text_prompt: str, token_limit:int, stop_sequences: list[str] = None, temperature:float = 0.0,timeout:float=600):
    API_KEY = os.environ.get('ANTHROPIC_API_KEY')   
    if not API_KEY:
        raise ValueError("ANTHROPIC_API_KEY environment variable not found")    
    
    try:
        anthropic_client = anthropic.Anthropic(api_key=API_KEY)
        messages = [{"role": "user", "content": text_prompt}]
        params = {
            'model': model_name,
            'max_tokens': token_limit,
            'temperature':temperature,
            'system': system_message,
            'messages': messages
        }

        if stop_sequences is not None:
            params['stop_sequences'] = stop_sequences

        response = anthropic_client.messages.create(**params,timeout=timeout)
        return response
    except Exception as e:
        current_app.logger.error(f"anthropic_request_prompt error: {e}")


def anthropic_get_response_content(anthropic_response):
    try:
        textblock = anthropic_response.content[0]
        text = textblock.text
        return text
    except Exception as e:
        current_app.logger.error(f"anthropic_get_response_content error: {e}")
