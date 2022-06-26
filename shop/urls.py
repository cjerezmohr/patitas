from django.urls import path
from shop.views import *
urlpatterns = [
    path('pet_food', pet_food, name = 'food'),
    path('pet_toys', pet_toys, name = 'toys'),
    path('pet_vet', pet_vet, name = 'vet'),
]