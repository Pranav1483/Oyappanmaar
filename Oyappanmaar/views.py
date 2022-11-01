from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Credentials

def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render({}, request))

def check(request):
    text = 'Welcome'
    username = request.POST.get('user', False)
    password = request.POST.get('passkey', False)
    if not username:
        text = 'Please Enter Username'
    else:
        flag = 0
        creds = Credentials.objects.all().values()
        for x in creds:
            if username == x['username']:
                flag = 1
                if password == x['password']:
                     text = 'Welcome ' + x['name']
                     flag = 2
                break
        if flag == 0:
            text = 'No User Found'
        elif flag == 1:
            text = 'Wrong Password'
    template = loader.get_template('dashboard.html')
    context = {
        'text': text
    }
    return HttpResponse(template.render(context, request))
            
            
        
    

