# Create your views here.

from django.shortcuts import render

import requests
import json
import sys
import os

class SteamClient(object):
    url = "http://api.steampowered.com/"
    url_services = {
        "friends": "ISteamUser/GetFriendList/v0001/",
        "player": "ISteamUser/GetPlayerSummaries/v0002/",
        "game": "ISteamNews/GetNewsForApp/v0002/",
        "Logros_player":"ISteamUserStats/GetPlayerAchievements/v0001/",
        "Own_games":"IPlayerService/GetOwnedGames/v0001/",
    }

    def __init__(self, userid, api_key):
        super(SteamClient, self).__init__()
        self.userid = userid
        self.api_key = api_key

    @property
    def getFriends(self):
        url_api = "?key=" + self.api_key + "&steamid=" + self.userid + "/&relationship=friend"
        url_ = SteamClient.url + SteamClient.url_services["friends"] + url_api
        request = requests.get(url_)
        l = []
        data = json.loads(request.text)
        for i in data["friendslist"]["friends"]:
            l.append(i["steamid"])


        m = []
        for i in l:
            url_api = "?key=" + self.api_key + "&steamids=" + i + "/"
            url_ = SteamClient.url + SteamClient.url_services["player"] + url_api

            request_1 = requests.get(url_)
            data1 = json.loads(request_1.text)
            for j in data1["response"]["players"]:
                m.append(j["personaname"])

        return m

    def StatsGame(self):
        url_api = "?appid=" + self.api_key + "&count=1&maxlength=2000&format=json"
        url_ = SteamClient.url + SteamClient.url_services["game"] + url_api
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

    def PlayerSummaries(self):
        url_api = "?key=" + self.api_key + "&steamids=" + self.userid + "/"
        url_ = SteamClient.url + SteamClient.url_services["player"] + url_api
        apodo=[]
        realname=[]
        country=[]

        request_1 = requests.get(url_)
        data1 = json.loads(request_1.text)
        for j in data1["response"]["players"]:
            apodo.append(j["personaname"])
            realname.append(j["realname"])
            country.append(j["loccountrycode"])



    def AchievementsPlayer(self):
        url_api = "?appid="+self.game+"&key=" + self.api_key + "&steamid=" + self.userid
        url_ = SteamClient.url + SteamClient.url_services["Logros_player"] + url_api
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
        url_ = SteamClient.url + SteamClient.url_services["Own_games"] + url_api

        request_1 = requests.get(url_)
        data1 = json.loads(request_1.text)
        lista_juegos=[]
        for j in data1["response"]["games"]:
            lista_juegos(j["appid"])

        for i in lista_juegos:
            url_api = "?appid=" + i + "&count=1&maxlength=2000&format=json"
            url_ = SteamClient.url + SteamClient.url_services["game"] + url_api
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


if __name__ == "__main__":
    api = sys.argv[1]
    id = sys.argv[2]
    client = SteamClient(id, api)
    print (client.getFriends)



