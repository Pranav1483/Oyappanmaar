from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Credentials, Note, NotePublic, Allowed
from django.shortcuts import redirect


def index(request):
    request.session['flag1'] = 0
    template = loader.get_template('Login.html')
    context = {
        'test': request.session.get('flag', -1),
    }
    return HttpResponse(template.render(context, request))


def check(request):
    user = request.POST.get('user', False)
    pwd = request.POST.get('pwd', False)
    if not user:
        user = request.session['user']
    else:
        request.session['user'] = user
    if not pwd:
        pwd = request.session['pwd']
    else:
        request.session['pwd'] = pwd
    creds = Credentials.objects.all().values()
    request.session['flag'] = 0
    for x in creds:
        if x['username'] == user:
            if x['password'] == pwd:
                request.session['flag'] = 2
                break
            else:
                request.session['flag'] = 1
                break
    if request.session['flag'] == 2:
        template = loader.get_template('DashBoard.html')
        context = {
            'privatenotes': Note.objects.get(user=user),
            'publicnotes': NotePublic.objects.all().values(),
            'member': Credentials.objects.get(username=user)
        }
        return HttpResponse(template.render(context, request))
    return HttpResponseRedirect(reverse('index'))


def new_user(request):
    template = loader.get_template('NewUser.html')
    context = {
        'c': request.session.get('flag1', 0)
    }
    return HttpResponse(template.render(context, request))


def add_user(request):
    a = request.POST['name']
    x = request.POST['user']
    y = request.POST['pwd']
    request.session['flag1'] = 2
    for iter in Allowed.objects.all().values():
        if iter['roll'] == x:
            request.session['flag1'] = 0
            break
    if request.session['flag1'] == 0:
        for iter in Credentials.objects.all().values():
            if iter['username'] == x:
                request.session['flag1'] = 1
                break
    if request.session['flag1'] == 0:
        request.session['flag'] = -1
        cred = Credentials(person=a, username=x, password=y)
        note = Note(user=x, name=a, notes='', l=0)
        notes = NotePublic(user=x, name=a, notes='', l=0)
        cred.save()
        notes.save()
        note.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        request.session['flag'] = -1
        return HttpResponseRedirect(reverse('new_user'))


def logout(request):
    return HttpResponseRedirect(reverse('index'))


def addp(request, id):
    member = Note.objects.get(user=id)
    cred = Credentials.objects.get(username=id)
    template = loader.get_template('AddPersonal.html')
    context = {
        'member': member,
        'cred': cred
    }
    return HttpResponse(template.render(context, request))


def addpfinal(request, id):
    data = request.POST['text']
    member = Note.objects.get(user=id)
    member.notes = data
    member.l = len(data)
    member.save()
    return HttpResponseRedirect(reverse('check'))


def addP(request, id):
    member = NotePublic.objects.get(user=id)
    cred = Credentials.objects.get(username=id)
    template = loader.get_template('AddPublic.html')
    context = {
        'member': member,
        'cred': cred
    }
    return HttpResponse(template.render(context, request))


def addPfinal(request, id):
    data = request.POST['text']
    member = NotePublic.objects.get(user=id)
    member.notes = data
    member.l = len(data)
    member.save()
    return HttpResponseRedirect(reverse('check'))
        
    
        
    

