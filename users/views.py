from django.shortcuts import render, redirect
from django.contrib import messages
from authentication.models import Management
from .models import Customers

def register(request):
    return render(request, 'register.html')

def home(request):
    if request.method == 'GET':
        customers = Customers.objects.all() 
        return render(request, 'home.html', {'customers': customers}) 


def management(request):
    if request.method == 'GET':
        return render(request, 'management.html')
    
    username = request.POST.get('nome')
    password = request.POST.get('password')

    if not username or not password:
        messages.error(request, "Todos os campos são obrigatórios.")
        return redirect('management')
    
    if Management.objects.filter(name=username, password=password).exists():
        messages.error(request, "O usuário já está em uso.")

    try:
        management = Management(name=username, password=password)
        management.save()

        return redirect('home')
    
    except Exception as e:

        messages.error(request, f"Ocorreu um erro")
        return redirect('management')