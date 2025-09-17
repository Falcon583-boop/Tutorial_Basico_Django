from django.shortcuts import render
from django.contrib import messages

def home(request):
    messages.success(request, "Bienvenido a la Biblioteca Django")
    return render(request, 'home.html')