import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')
def about(request):
    return render(request, 'generator/about.html')
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list( ' !@#$%^&*( )'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    length = int(request.GET.get('length', 122))  
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
