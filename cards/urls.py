from django.urls import path
from . import views

app_name = "cards"


urlpatterns = [
    path('',views.all_cards,name='all_cards'),
]