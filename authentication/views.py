from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Management

def authentication(request):
    if request.method == 'GET':
        return render(request, 'authentication.html')

    else:
        username = request.POST.get('usuario')
        password = request.POST.get('password')

        if username == '' or password == '':
            messages.error(request, 'Usuário Inválido.')
            return redirect('authentication')
        
        if Management.objects.filter(name=username, password=password).exists():
            request.session['is_authenticated'] = True
            return render(request, 'home.html')
        else:
            messages.error(request, f"Usuário inválido.")
            return redirect('authentication')