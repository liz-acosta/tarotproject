from django.urls import path

from . import views
from .views import FiveCardsView

urlpatterns = [
    # tarot/
    path("", views.index, name="index"),
    # tarotapp/cut_deck/
    path("cut_deck/", views.cut_deck, name="cut_deck"),
    # tarotapp/five_cards/
    path("five_cards/", FiveCardsView.as_view(), name="five_cards"),
]