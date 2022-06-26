from django.shortcuts import render

from Petshop.shop.models import *

# Create your views here.

def pet_food(request):
    new_food = Pet_food.objects.all()
    context = {'new_food':new_food}
    return render(request, 'food.html', context = context)

def pet_toys(request):
    new_toy = Pet_toys.objects.all()
    context = {'new_toy':new_toy}
    return render(request, 'toys.html', context = context)

def pet_vet(request):
    new_vet = Pet_vet.objects.all()
    context = {'new_vet':new_vet}
    return render(request, 'vet.html', context = context)