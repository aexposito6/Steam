# Create your views here.

from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import requests
import json
from forms import UserForm
from models import UserProfile

url = "http://api.steampowered.com/"
url_services = {
    "friends": "ISteamUser/GetFriendList/v0001/",
    "player": "ISteamUser/GetPlayerSummaries/v0002/",
    "game": "ISteamNews/GetNewsForApp/v0002/",
    "Logros_player":"ISteamUserStats/GetPlayerAchievements/v0001/",
    "Own_games":"IPlayerService/GetOwnedGames/v0001/",
}

def getFriends(request):
    context = RequestContext(request)
    #charname = request.GET.get('name')
    if request.user.is_authenticated():
        user = User.objects.get(id=request.user.id)
        profile = UserProfile.objects.filter(user=user).get()
        api = profile.apikey
        id = profile.id_user
    url_api = "?key=" + str(api) + "&steamid=" + str(id) + "/&relationship=friend"
    url_ = url + url_services["friends"] + url_api
    request = requests.get(url_)
    l = []
    data = json.loads(request.text)
    for i in data["friendslist"]["friends"]:
        l.append(i["steamid"])


    m = []
    for i in l:
        url_api = "?key=" + api + "&steamids=" + i + "/"
        url_ = url + url_services["player"] + url_api

        request_1 = requests.get(url_)
        data1 = json.loads(request_1.text)
        for j in data1["response"]["players"]:
            m.append(j["personaname"])
            m.append(i)

    return render_to_response('friends.html',{'friends': m},context)

def StatsGame(self):
    url_api = "?appid=" + self.api_key + "&count=1&maxlength=2000&format=json"
    url_ = url + url_services["game"] + url_api
    request = requests.get(url_)

    print url_
    contenido = []
    titulo = []
    autor = []
    data = json.loads(request.text)

    for i in data["appnews"]["newsitems"]:

        contenido.append(i["contents"])
        titulo.append(i["title"])
        autor.append(i["author"])
def FriendSummaries(request):
    context = RequestContext(request)
    # charname = request.GET.get('name')
    if request.user.is_authenticated():
        user = User.objects.get(id=request.user.id)
        profile = UserProfile.objects.filter(user=user).get()
        api = profile.apikey
        id = profile.id_user
    url_api = "?key=" + str(api) + "&steamid=" + str(id) + "/&relationship=friend"
    url_ = url + url_services["friends"] + url_api
    request = requests.get(url_)
    l = []
    data = json.loads(request.text)
    for j in data1["response"]["players"]:
        apodo.append(j["personaname"])
        realname.append(j["realname"])
        country.append(j["loccountrycode"])
def PlayerSummaries(request):
    context = RequestContext(request)
    # charname = request.GET.get('name')
    if request.user.is_authenticated():
        user = User.objects.get(id=request.user.id)
        profile = UserProfile.objects.filter(user=user).get()
        api = profile.apikey
        id = profile.id_user
    url_api = "?key=" + str(api) + "&steamid=" + str(id) + "/&relationship=friend"
    url_ = url + url_services["friends"] + url_api
    request = requests.get(url_)
    l = []
    data = json.loads(request.text)
    apodo = []
    realname = []
    country = []
    imagen = []
    for j in data["response"]["players"]:
        apodo.append(j["personaname"])
        realname.append(j["realname"])
        country.append(j["loccountrycode"])
        imagen.append(j["avatarmedium"])

    return render_to_response('UserData.html', {'apodo': apodo, 'realname': realname, 'country': country, 'imagen': imagen}, context)
def AchievementsPlayer(self):
    url_api = "?appid="+self.game+"&key=" + self.api_key + "&steamid=" + self.userid
    url_ = url + url_services["Logros_player"] + url_api
    request = requests.get(url_)
    data = json.loads(request.text)
    contador=0
    logros=[]
    resultado=[]
    for j in data["playerstats"]["Achievements"]:

        if contador<10:
            logros.append(j["Apiname"])
            resultado.append(j["Achieved"])
        contador=contador+1
#ttp://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=XXXXXXXXXXXXXXXXX&steamid=76561197960434622&format=json

def OwnGame(self):
    url_api = "?key=" + self.api_key + "&steamids=" + self.userid + "&format=json"
    url_ = url + url_services["Own_games"] + url_api

    request_1 = requests.get(url_)
    data1 = json.loads(request_1.text)
    lista_juegos=[]
    for j in data1["response"]["games"]:
        lista_juegos(j["appid"])

    for i in lista_juegos:
        url_api = "?appid=" + i + "&count=1&maxlength=2000&format=json"
        url_ = url + url_services["game"] + url_api
        request = requests.get(url_)

        print url_
        contenido = []
        titulo = []
        autor = []
        data = json.loads(request.text)

        for i in data["appnews"]["newsitems"]:
            contenido.append(i["contents"])
            titulo.append(i["title"])
            autor.append(i["author"])

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
    return render_to_response("mainpage.html", context)




