from django.shortcuts import render
from .models import Card
# Create your views here.
def all_cards(request):
    cards = Card.objects.all()
    return render(request,'cards/all_cards.html',{'cards':cards})