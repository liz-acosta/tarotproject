
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views import View

from .forms import SendTextForm
from .models import TarotCard
from .tarot_reading import get_final_three_cards, get_ai_reading

from twilio.rest import Client


def index(request):
    # Card shuffling page
    
    template = "tarotapp/index.html"
    
    text ="""
    As you walk along a murky path, you encounter a dark shape. 
    As you draw closer to it, you realize it's a hooded stranger. 
    A hand beckons from within the depths of the stranger's robes. 
    With apprehension, you peer closer, and see that the stranger is shuffling a deck of cards.
    """
    context = {"text": text,}

    return render(request, template, context)


def cut_deck(request):
    # Cut the deck page
    
    template = "tarotapp/card_table.html"

    text ="""
    The robed figure asks you to cut the deck, and you do so with great trepidation.
    With a voice like gravel, the figure tells you to select a deck.
    """
    cut_deck_image = "53c0cce811d9a_thumb900.jpg"
    context = {
        "text": text,
        "cut_deck_image": cut_deck_image,}

    return render(request, template, context)


class FiveCardsView(View):
    # Five cards page

    def get(self, request):

        template = "tarotapp/five_cards.html"
        text = """
        You make your choice! 
        Five cards are dealt from the deck and laid out before you. 
        Your job is to choose the final three cards to reveal your fate.
        """
        cut_deck_image = "53c0cce811d9a_thumb900.jpg"

        text_message_form = SendTextForm()  

        final_cards = get_final_three_cards()
        tarot_reading = get_ai_reading(final_cards) 

        context = {
        "text": text,
        "cut_deck_image": cut_deck_image,
        'final_cards': final_cards,
        'tarot_reading': tarot_reading,
        'text_message_form': text_message_form}
        
        return render(request, template, context)

    def post(self, request):
        
        form = SendTextForm(request.POST) 
        # Bind form data from the request

        phone_number = request.POST['phone_number']
        tarot_reading = request.POST['tarot_reading']

        # openai.api_key = settings.OPENAI_KEY
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                    body=tarot_reading,
                                    from_='+18336330410',
                                    to=phone_number,
                                )

        print(message.sid)

        print("*****", phone_number)
        
        return redirect('index')


def final_cards(request):
    # Final cards page

    template = "tarotapp/final_cards.html" 
    
    text = "Here are your cards ..."
    context = {
    "text": text,
    "cut_deck_image": cut_deck_image,}
    
    return render(request, template, context)