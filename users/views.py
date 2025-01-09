from django.shortcuts import render

def register(request):
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')

def management(request):
    return render(request, 'management.html')
