import random

def handle_response(messages) -> str:
    p_message = messages.lower()


    if p_message == 'hello':
        return 'Hey there!'
    
    if p_message == 'roll':
        return str(random.randint(1,6))
    
    if p_message == '!help':
        return f"Go fuck yourself, how's that for help?"

def mean_response(user) -> str:
    return f'{user} tried to speak.'
    