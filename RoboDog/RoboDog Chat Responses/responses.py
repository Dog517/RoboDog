import discord
import random
authorusername= ""
heilarray = ['Seig heil!', 'Heil Hitler!', 'Heil, mein Führer!']

def handle_response(message) -> str:
    p_message = message.lower()
    if 'gun' in p_message:
        return 'Murica!'
    if 'football' in p_message and not 'american' in p_message and authorusername == 'moroccandudelmao' or authorusername == 'rayan123go':
        return 'Its soccer, non-American!'
    if 'gun' in p_message:
        return 'Murica!'
    if 'pizza' in p_message:
        return 'Pizza is the food of the master race!'
    if 'hitler' in p_message or 'heil' in p_message:
        heilrandom = random.choice(heilarray)
        return heilrandom
    if 'amog' in p_message or 'sus' in p_message or 'among us' in p_message or 's u s' in p_message:
        return '***s u s***'
    
