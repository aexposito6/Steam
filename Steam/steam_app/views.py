# Create your views here.


from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import requests
import json
#from forms import UserForm
from forms import UserForm
from models import UserProfile
'''
url = "http://api.steampowered.com/"
url_services = {
    "friends": "ISteamUser/GetFriendList/v0001/",
    "player": "ISteamUser/GetPlayerSummaries/v0002/",
    "game": "ISteamUserStats/GetPlayerAchievements/v0001/",
    "Logros_player":"ISteamUserStats/GetPlayerAchievements/v0001/",
    "Own_games":"IPlayerService/GetOwnedGames/v0001/",
    "version":"ISteamUserStats/GetSchemaForGame/v2/",
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

    a = 0
    b = 1
    m = []
    tmp = []
    for i in l:
        url_api = "?key=" + api + "&steamids=" + i + "/"
        url_ = url + url_services["player"] + url_api

        request_1 = requests.get(url_)
        data1 = json.loads(request_1.text)
        for j in data1["response"]["players"]:
            tmp = []
            tmp.append(j["personaname"])
            tmp.append(i)
            m.append(tmp)


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
def FriendSummaries(request, id_friend):
    context = RequestContext(request)
    # charname = request.GET.get('name')
    if request.user.is_authenticated():
        user = User.objects.get(id=request.user.id)
        profile = UserProfile.objects.filter(user=user).get()
        api = profile.apikey
    url_api = "?key=" + str(api) + "&steamids=" + str(id_friend) + "/"
    url_ = url + url_services["player"] + url_api
    request = requests.get(url_)
    data = json.loads(request.text)
    imagen = "Valor no definido"
    apodo = "Valor no definido"
    realname = "Valor no definido"
    profile = "Valor no definido"
    country = "Valor no definido"
    for j in data["response"]["players"]:
        apodo = j["personaname"]
        if "realname" in data["response"]["players"]:
            realname = j["realname"]
        if "loccountrycode" in data["response"]["players"]:
            country = j["loccountrycode"]
        profile = j["profileurl"]
        imagen = j["avatarmedium"]
    return render_to_response('datos_amigos.html', {'imagen': imagen, 'realname': realname, 'country': country, 'profile': profile, 'apodo': apodo, 'id': id_friend}, context)

def PlayerSummaries(request):
    context = RequestContext(request)
    # charname = request.GET.get('name')
    if request.user.is_authenticated():
        user = User.objects.get(id=request.user.id)
        profile = UserProfile.objects.filter(user=user).get()
        api = profile.apikey
        id = profile.id_user
    url_api = "?key=" + str(api) + "&steamids=" + str(id) + "/"
    url_ = url + url_services["player"] + url_api
    request = requests.get(url_)
    l = []
    data = json.loads(request.text)
    for j in data["response"]["players"]:
        apodo = j["personaname"]
        realname = j["realname"]
        country = j["loccountrycode"]
        profile = j["profileurl"]
        imagen = j["avatarmedium"]

    return render_to_response('UserData.html', {'apodo': apodo, 'realname': realname, 'country': country, 'profile': profile, 'imagen': imagen}, context)
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
    return render_to_response('Achievements.html', {'friends': m}, context)
#ttp://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=XXXXXXXXXXXXXXXXX&steamid=76561197960434622&format=json

def OwnGame(request):
    context = RequestContext(request)
    # charname = request.GET.get('name')
    if request.user.is_authenticated():
        user = User.objects.get(id=request.user.id)
        profile = UserProfile.objects.filter(user=user).get()
        api = profile.apikey
        id = profile.id_user



    url_api = "?key=" + str(api) + "&steamid=" + str(id) + "&format=json"
    url_ = url + url_services["Own_games"] + url_api

    request_1 = requests.get(url_)
    data1 = json.loads(request_1.text)
    lista_juegos=[]
    for j in data1["response"]["games"]:
        lista_juegos.append(j["appid"])
    name = []
    version=[]
    for i in lista_juegos:
        url_api = "?appid="+str(i)+"&key=" + str(api) + "&steamid="+str(id)
        url_ = url + url_services["game"] + url_api
        request = requests.get(url_)



        data = json.loads(request.text)
        if "gameName" in data ["playerstats"].keys():
            name.append(data["playerstats"]["gameName"])

        url_api2 = "?key=" + str(api)  + "&appid=" + str(i)
        url_2 = url + url_services["version"] + url_api2
        request2 = requests.get(url_2)
        data2 = json.loads(request2.text)
        if "gameVersion" in data2 ["game"].keys():

            version.append(data2["game"]["gameVersion"])
        v=len(version)
    return render_to_response('GameData.html', {'version':version,'name':name,'long':v}, context)
'''
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




