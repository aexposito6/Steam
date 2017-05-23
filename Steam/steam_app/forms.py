from django import forms
from django.contrib.auth.models import User
from models import Game, UserProfile

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
class UserProfileForm(forms.ModelForm):
    class Meta:
        model =UserProfile
        fields=('user','id','steam_id','nickname','real_name','country','city','url_profile','friends')
        exclude = ('user','id')


