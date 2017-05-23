from django import forms
from django.contrib.auth.models import User
from models import Game, Clan, Achievement, UserProfile
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('user', 'id','appid', 'name','version', 'company', 'opinion')
        exclude = ('user', 'id', )

class ClanForm (forms.ModelForm):
    class Meta:
        model = Clan
        fields = ('user', 'id', 'name','number_of_person','members')
        exclude = ('user', 'id')
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=('user','id','steam_id','nickname','real_name','city','stateOrProvince','country','url_profile','friends')
        exclude = ('user','id')
class AchievementForm (forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ('user', 'id', 'appid_game','name','achieved')
        exclude = ('user', 'id')
