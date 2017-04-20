from django import forms
from django.contrib.auth.models import User

from models import UserProfile, Game, Achievement, Clan

'''class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user','steam_id', 'name_steam', 'real_name', 'country', 'profile',)

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('user','appid', 'name', 'version','id_user',)

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ( 'name_achi', 'done',)

class ClanForm(forms.ModelForm):
    class Meta:
        model = Clan
        fields = ('id_clan', 'name', 'number_of_members',)
'''
'''
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user',)

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('user',)

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ('user',)

class ClanForm(forms.ModelForm):
    class Meta:
        model = Clan
        fields = ('user',)
'''