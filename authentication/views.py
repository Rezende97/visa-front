from django.shortcuts import render
from django.http import HttpResponse

def authentication(request):

    if request.method == 'GET':
        return render(request, 'authentication.html')
    else:

        username = request.POST.get('username')
        
        if username == '':
            return HttpResponse('esta vazio')

        return render(request, 'home.html')
        
