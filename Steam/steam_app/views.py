# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, generics

import forms
from serializers import UserProfileSerializer, GameSerializer, AchievementSerializer, ClanSerializer
from forms import UserForm, GameForm, ClanForm, AchievementForm
from models import UserProfile, Game, Clan, Achievement


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
@login_required
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
@login_required
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
@login_required
def delete_game(request, id_game):
    game = Game.objects.get(pk=id_game)
    game.delete()
    return render(request, "delete_game.html", {})
@login_required
def after_change_game(request):
    context = RequestContext(request)
    return render_to_response("update_game.html", {}, context)
@login_required
def after_game(request):
    context = RequestContext(request)
    return render_to_response("game_created.html", {}, context)

@csrf_exempt
@login_required
def clan(request):
    if request.method=="POST":
        ClanForm=forms.ClanForm(data=request.POST)
        if ClanForm.is_valid():
            clan = Clan(user=request.user,name=ClanForm.cleaned_data['name'],
                             number_of_person=ClanForm.cleaned_data['number_of_person'],
                            members=ClanForm.cleaned_data['members']
                             )
            clan.save()
            return HttpResponseRedirect('/clan/sent')
        else:
            print(ClanForm.errors)
    else:
        ClanForm=forms.ClanForm()

    return render(request,"clan.html", {'ClanForm':ClanForm})
@csrf_exempt
@login_required
def after_clan(request):
    context = RequestContext(request)
    return render_to_response("clan_created.html", {}, context)
@login_required
def print_clan(request):
    l = []
    u = User.objects.get(username__exact=request.user)
    for i in Clan.objects.all():
        if i.user == u:
            l.append(i)
    return render(request, "list_clan.html", {'list': l})
@csrf_exempt
@login_required
def change_clan(request, id_clan):
    clan = get_object_or_404(Clan, pk=id_clan)
    if request.method == "POST":
        clan_form = forms.ClanForm(request.POST, instance=clan)
        if clan_form.is_valid():
            clan_form.save()
            return HttpResponseRedirect('/change/clan/done')
        else:
            clan = Clan.objects.get(pk=id_clan)
            ClanForm = forms.ClanForm(instance=clan)
    else:
        ClanForm = forms.ClanForm(instance=clan)

    return render(request, "edit_clan.html", {'ClanForm': ClanForm})
@csrf_exempt
@login_required
def delete_clan(request, id_clan):
    clan = Clan.objects.get(pk=id_clan)
    clan.delete()
    return render(request, "delete_clan.html", {})
@csrf_exempt
@login_required
def after_change_clan(request):
    context = RequestContext(request)
    return render_to_response("update_clan.html", {}, context)


@csrf_exempt
@login_required
def achievement(request):
    achi = AchievementForm(data=request.POST)
    achi.fields['appid_game'].queryset = Game.objects.filter(user=request.user)
    if request.method=="POST":
        if achi.is_valid():
            achievement = Achievement(user=request.user,name= achi.cleaned_data['name'],
                             appid_game=(achi.cleaned_data['appid_game']),
                            achieved=achi.cleaned_data['achieved']
                             )
            achievement.save()
            return HttpResponseRedirect('/achievement/sent')
        else:
            print(achi.errors)
    else:
        achievement=achi

    return render(request,"Achievements.html", {'AchievementForm':achievement})
@csrf_exempt
@login_required
def after_achievement(request):
    context = RequestContext(request)
    return render_to_response("achievement_created.html", {}, context)
@login_required
def print_achievement(request):
    l = []
    u = User.objects.get(username__exact=request.user)
    for i in Achievement.objects.all():
        if i.user == u:
            l.append(i)
    return render(request, "list_achievement.html", {'list': l})
@csrf_exempt
@login_required
def change_achievement(request, id_achievement):
    achievement = get_object_or_404(Achievement, pk=id_achievement)
    if request.method == "POST":
        achievement_form = forms.AchievementForm(request.POST, instance=achievement)
        if achievement_form.is_valid():
            achievement_form.save()
            return HttpResponseRedirect('/change/achievement/done')
        else:
            achievement = Achievement.objects.get(pk=id_achievement)
            AchievementForm = forms.AchievementForm(instance=achievement)
    else:
        AchievementForm = forms.AchievementForm(instance=achievement)

    return render(request, "edit_achievement.html", {'AchievementForm': AchievementForm})
@csrf_exempt
@login_required
def delete_achievement(request, id_achievement):
    achievement = Achievement.objects.get(pk=id_achievement)
    achievement.delete()
    return render(request, "delete_achievement.html", {})
@csrf_exempt
@login_required
def after_change_achievement(request):
    context = RequestContext(request)
    return render_to_response("update_achievement.html", {}, context)
@login_required
def user(request):
    if request.method=="POST":
        UserForm=forms.UserProfileForm(data=request.POST)
        if UserForm.is_valid():
            user = UserProfile(user=request.user, steam_id=UserForm.cleaned_data['steam_id'],nickname=UserForm.cleaned_data['nickname'],
                             real_name=UserForm.cleaned_data['real_name'],city=UserForm.cleaned_data['city'],stateOrProvince=UserForm.cleaned_data['stateOrProvince'], country=UserForm.cleaned_data['country'],
                         friends=UserForm.cleaned_data['friends'])
            user.save()
            return HttpResponseRedirect('/user/sent')
        else:
            print(UserForm.errors)
    else:
        UserForm=forms.UserProfileForm()

    return render(request,"user.html", {'UserForm':UserForm})
@login_required
def after_user(request):
    context = RequestContext(request)
    return render_to_response("user_created.html", {}, context)
@login_required
def print_users(request):
    l = []
    u = User.objects.get(username__exact=request.user)
    for i in UserProfile.objects.all():
        if i.user == u:
            l.append(i)
    return render(request, "list_user.html", {'list': l})
@login_required
def change_user(request, id_user):
    user = get_object_or_404(UserProfile, pk=id_user)
    if request.method == "POST":
        user_form = forms.UserProfileForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect('/change/user/done')
        else:
            user = UserProfile.objects.get(pk=id_user)
            UserProfileForm = forms.UserProfileForm(instance=user)
    else:
        UserProfileForm = forms.UserProfileForm(instance=user)
    return render(request, "edit_user.html", {'UserProfileForm': UserProfileForm})
@login_required
def after_change_user(request):
    context = RequestContext(request)
    return render_to_response("update_user.html", {}, context)
@login_required
def delete_user(request, id_user):
    user = UserProfile.objects.get(pk=id_user)
    user.delete()
    return render(request, "delete_user.html", {})
@login_required
def api_page(request):
    context = RequestContext(request)
    return render_to_response("api.html", {}, context)

class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.UserProfile.user == request.user

class APIUserProfileList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = UserProfile
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class APIUserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = permissions.IsAuthenticatedOrReadOnly
    model = UserProfile
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class APIGameList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = Game
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class APIGameDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = permissions.IsAuthenticatedOrReadOnly
    model = Game
    queryset = Game.objects.all()
    serializer_class = GameSerializer
class APIAchievementList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = Achievement
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class APIAchievementDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = permissions.IsAuthenticatedOrReadOnly
    model = Achievement
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
class APIClanList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = Clan
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class APIClanDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = permissions.IsAuthenticatedOrReadOnly
    model = Clan
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer

