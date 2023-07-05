from django.urls import path

from . import views
from .views import FiveCardsView

urlpatterns = [
    path("", views.index, name="index"),
    path("cut_deck/", views.cut_deck, name="cut_deck"),
    path("five_cards/", FiveCardsView.as_view(), name="five_cards"),
    path("final_cards/", views.final_cards, name="final_cards"),
]