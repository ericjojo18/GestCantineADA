from django.shortcuts import render, redirect
from django.contrib import messages
from cantine.models.menu_model import Menu
# Create your views here.

def home(request): 
    return render(request, 'index.html')

def index(request):
    menus = Menu.objects.all()
    context = {'menus': menus}
    return render(request, 'menus.html', context)

