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
    }
    #:  http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=440&count=3&maxlength=300&format=json

    def __init__(self, api_key):
        super(SteamClient, self).__init__()
       # self.userid = userid
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
        url_api="?appid="+self.api_key+"&count=1&maxlength=2000&format=json"
        url_ = SteamClient.url + SteamClient.url_services["game"]+url_api
        request=requests.get(url_)
        print url_
        l=[]
        l2=[]
        l3=[]
        data=json.loads(request.text)
        for i in data["appnews"]["newsitems"]:

            l.append(i["contents"])
            l2.append(i["title"])
            l3.append(i["author"])
        print l2

if __name__ == "__main__":
    api = sys.argv[1]
   # id = sys.argv[2]
    client = SteamClient(api)
    #print client.getFriends
    client.StatsGame()


