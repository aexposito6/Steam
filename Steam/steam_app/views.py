# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import requests
import json
#from forms import UserForm
import forms
from forms import UserForm, GameForm
from models import UserProfile, Game


@csrf_exempt
def register(request):

    context = RequestContext(request)


    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)


        if user_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print user_form.errors
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
        'registration/register.html',
        {'user_form': user_form, 'registered': registered},
        context)
def mainpage(request):

    context = RequestContext(request)
    return render_to_response("mainpage.html",{}, context)

def after_login(request):
    context = RequestContext(request)
    return render_to_response("after_login.html", {}, context)

def after_logout(request):
    context = RequestContext(request)
    return render_to_response("logout.html", {}, context)
@csrf_exempt

def games(request):
    context = RequestContext(request)
    if request.method=="POST":
        GameForm=forms.GameForm(data=request.POST)
        if GameForm.is_valid():
            opinio = Game(appid=GameForm.cleaned_data['appid'],name=GameForm.cleaned_data['name'],
                             version=GameForm.cleaned_data['version'], company=GameForm.cleaned_data['company'],
                             news=GameForm.cleaned_data['news'])
            opinio.save()
            return HttpResponseRedirect('/game/sent')
        else:
            print(GameForm.errors)
    else:
        GameForm=forms.GameForm()

    return render(request,"game.html", {'GameForm':GameForm})

def after_game(request):
    context = RequestContext(request)
    return render_to_response("game_created.html", {}, context)




