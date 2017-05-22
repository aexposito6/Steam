# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext

from django.views.decorators.csrf import csrf_exempt
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

def after_logout(request):
    context = RequestContext(request)
    return render_to_response("logout.html", {}, context)
@csrf_exempt
@login_required()
def games(request):
    if request.method=="POST":
        GameForm=forms.GameForm(data=request.POST)
        if GameForm.is_valid():
            game = Game(user=request.user, appid=GameForm.cleaned_data['appid'],name=GameForm.cleaned_data['name'],
                             version=GameForm.cleaned_data['version'], company=GameForm.cleaned_data['company'],
                             opinion=GameForm.cleaned_data['opinion'])
            game.save()
            return HttpResponseRedirect('/game/sent')
        else:
            print(GameForm.errors)
    else:
        GameForm=forms.GameForm()

    return render(request,"game.html", {'GameForm':GameForm})
def print_games(request):
    l = []
    u = User.objects.get(username__exact=request.user)
    for i in Game.objects.all():
        if i.user == u:
            l.append(i)
    return render(request, "list_game.html", {'list': l})
@csrf_exempt
@login_required
def change_game(request, id_game):
    game = get_object_or_404(Game, pk=id_game)
    if request.method == "POST":
        game_form = forms.GameForm(request.POST, instance=game)
        if game_form.is_valid():
            game_form.save()
            return HttpResponseRedirect('/change/game/done')
        else:
            game = Game.objects.get(pk=id_game)
            GameForm = forms.GameForm(instance=game)
    else:
        GameForm = forms.GameForm(instance=game)

    return render(request, "edit_game.html", {'GameForm': GameForm})
def delete_game(request, id_game):
    game = Game.objects.get(pk=id_game)
    game.delete()
    return render(request, "delete_game.html", {})
def after_change_game(request):
    context = RequestContext(request)
    return render_to_response("update_game.html", {}, context)

def after_game(request):
    context = RequestContext(request)
    return render_to_response("game_created.html", {}, context)




