from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

import json
# Create your models here.

#from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


'''class UserProfile (models.Model):
    user = models.ForeignKey(User,default=1)
    steam_id = models.ManyToManyField('Game', 'Clan')
    name_steam = models.TextField(blank=True, null=True)
    real_name = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    profile = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.user.username
class Game (models.Model):
    user = models.ForeignKey(User,default=1)
    appid = models.ForeignKey('Achievement')
    name = models.TextField(blank=True, null=True)
    version = models.IntegerField()
    id_user = models.IntegerField()

class Achievement(models.Model):
    user = models.ForeignKey(User, default=1)
    id_game = models.ForeignKey('Game')
    id_user = models.ForeignKey('UserProfile')
    name_achi = models.TextField(blank=True, null=True)
    done = models.BooleanField()

class Clan(models.Model):
    user = models.ForeignKey(User, default=1)
    id_clan = models.IntegerField()
    id_user = models.ForeignKey('UserProfile')
    name = models.TextField(blank=True, null=True)
    number_of_members = models.IntegerField()
'''
class UserProfile(models.Model):
    #user = models.OneToOneField(User)
    steam_id = models.IntegerField(blank=True, null = True)
    name = models.CharField(max_length=50, blank=True, null=True)
    real_name=models.CharField(max_length=50, blank=True, null=True)
    country=models.CharField(max_length=50, blank=True, null=True)
    url_profile=models.CharField(max_length=50, blank=True, null=True)
    #avatar=models.ImageField()
    friends=models.TextField(null=True)
    def __unicode__(self):
        return str(self.name)
class Game (models.Model):
    id_user = models.ForeignKey(UserProfile, blank=True, null = True)
    appid = models.IntegerField(blank=True, null = True)
    name = models.CharField(max_length=50, blank=True, null=True)
    version= models.IntegerField(blank=True, null=True)
    company=models.CharField(max_length=50, blank=True, null=True)
    def __unicode__(self):
        return str(self.name)
class Achievement(models.Model):
    id_user = models.ForeignKey(UserProfile, blank=True, null=True)
    appid_game = models.ForeignKey(Game, blank=True, null=True)
    name=models.CharField(max_length=50, blank=True, null=True)
    done=models.BooleanField(default=False)
    def __unicode__(self):
        return str(self.name)
class Clan(models.Model):
    id_user = models.ForeignKey(UserProfile, blank=True, null=True)
    id_clan=models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    number_of_person=models.IntegerField(blank=True, null=True)
    members = models.TextField(null=True)
    def __unicode__(self):
        return str(self.name)