from django.conf import settings

from .models import TarotCard

import openai
from random import sample
from twilio.rest import Client


def get_final_three_cards():
    # Get final three cards from database
    
    card_ids_to_get = sample(range(78),3)
    print(card_ids_to_get)
    final_cards = []

    for id in card_ids_to_get:
        card = TarotCard.objects.get(pk=id)

        if card.arcana:
            card_name = card.symbol
        else:
            card_name = f"The {card.number} of {card.symbol}"
        
        card_object = {
            'card_name': card_name,
            'card_meaning': card.meaning,
            'card_image': card.image_filename}
        print(card_object)
        
        final_cards.append(card_object)

    return final_cards

def get_ai_reading(final_cards):
    # Make call to OpenAI to get tarot reading and return reading

    prompt = f"Give me a summarized tarot reading of the following cards: {final_cards[0]['card_name']}, {final_cards[1]['card_name']}, and {final_cards[2]['card_name']}"
    
    openai.api_key = settings.OPENAI_KEY
    openai_response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.3,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    tarot_reading = openai_response['choices'][0]['text']
    
    # tarot_reading = "test reading"
    
    return tarot_reading

def text_reading(to_number, tarot_reading):
    # Make call to Twilio to send reading to user given phone number

    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body=tarot_reading,
                                from_='+18336330410',
                                to=to_number,
                            )
    
    return message.sid

def a_func_that_does_nothing():
    print("nothing doing")
    return "nope"