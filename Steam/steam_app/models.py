from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    steam_id = models.IntegerField(unique=True,default=False)
    nickname = models.CharField(max_length=50, default='' , unique=True)
    real_name=models.CharField(max_length=50,blank=True, null=True)
    city = models.CharField(max_length=50, default='')
    stateOrProvince = models.CharField(max_length=50, blank=True, null=True)
    country=models.CharField(max_length=50, blank=True, null=True)
    url_profile=models.CharField(max_length=50, blank=True, null=True)
    #avatar=models.CharField(max_length=50, blank=True, null=True)
    friends=models.TextField(null=True, blank=True) #Para poder poner amigos que no esten registrados a nuestra app
    def get_absolute_url(self):
        return reverse('change_name', kwargs={'id_game': self.id})

    def __unicode__(self):
        return str(self.user.username)

class Game (models.Model):
    user = models.ForeignKey(User)
    appid = models.IntegerField(default=False)
    name = models.CharField(max_length=50, default='')
    version= models.FloatField(blank=True, null=True)
    company=models.CharField(max_length=50, blank=True, null=True)
    opinion = models.TextField(blank=True, null=True)
    def get_absolute_url(self):
        return reverse('change_name', kwargs={'id_game': self.id})
    def __unicode__(self):
        return str( "Juego: " + str(self.name))

class Achievement(models.Model):

    user = models.ForeignKey(User)
    appid_game = models.ForeignKey(Game, default=False)
    name = models.CharField(max_length=50, default='')
    achieved = models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse('change_achievement', kwargs={'id_achievement': self.id})
    def __unicode__(self):
        return str("Usuario: " + str(self.user) + "," + "Achievement: "+ str(self.name))


class Clan(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50, default='')
    number_of_person=models.IntegerField(blank=True, null=True)
    members = models.TextField(null=True, blank=True) #Para poder poner miembros que no esten regitrados a nuestra app
    def get_absolute_url(self):
        return reverse('change_clan', kwargs={'id_clan': self.id})
    def __unicode__(self):
        return str("Clan:" + self.name )

