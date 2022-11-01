from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Credentials, Allowed

def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render({}, request))


def check(request):
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
            

def new_user(request):
    template = loader.get_template('newuser.html')
    return HttpResponse(template.render({}, request))


def signup(request):
    name = request.POST.get('name', False)
    username = request.POST.get('user', False)
    password = request.POST.get('passkey', False)
    a = Allowed.objects.all().values()
    flag = 0
    for x in a:
        if x['username'] == username:
            flag = 1
            break
    if flag == 0:
        return HttpResponse("Not Oyappan")
    else:
        a = Credentials.objects.all().values()
        idx = 0
        for x in a:
            if x['username'] == username:
                return HttpResponse('User Already Exists')
            idx = max(idx, x['id'])
        tmp = Allowed(idx+1, name, username, password)
        tmp.save()
        return HttpResponseRedirect(reverse('homepage'))
        
    
        
    

